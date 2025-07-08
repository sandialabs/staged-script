#!/usr/bin/env python3
"""A staged script with a retryable stage."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import argparse
import functools
import platform
import socket
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Optional

from staged_script import RetryStage, StagedScript


class MyScript(StagedScript):
    def __init__(
        self,
        stages: set[str],
        *,
        console_force_terminal: Optional[bool] = None,
        console_log_path: bool = True,
        print_commands: bool = True,
    ):
        super().__init__(
            stages,
            console_force_terminal=console_force_terminal,
            console_log_path=console_log_path,
            print_commands=print_commands,
        )
        self.num_times_flaky_run = 0

    @StagedScript.stage("hello", "Greeting the user")
    def say_hello(self) -> None:
        self.run("echo 'Hello World'", shell=True)
        self.console.log(f"Processing file:  {self.args.some_file}")

    @StagedScript.stage("flaky", "Trying an error-prone operation")
    def try_error_prone_operation(self) -> None:
        self.num_times_flaky_run += 1
        num_times_to_fail = 2
        if self.num_times_flaky_run <= num_times_to_fail:
            self.console.log("[red]Oh no!  Something went horribly wrong!")
            self.script_success = False
            raise RetryStage
        self.console.log("[green]Thank goodness, everything worked this time.")
        self.script_success = True

    @StagedScript.stage("goodbye", "Bidding farewell")
    def say_goodbye(self) -> None:
        self.run("echo 'Goodbye World'", shell=True)
        self.console.log(
            "Some flag was " + ("not " if not self.flag else "") + "set!"
        )

    @functools.cached_property
    def parser(self) -> ArgumentParser:
        my_parser = super().parser
        my_parser.description = "Demonstrate adding arguments to the parser."
        self.hello_retry_attempts_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.hello_retry_delay_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.hello_retry_timeout_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.goodbye_retry_attempts_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.goodbye_retry_delay_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.goodbye_retry_timeout_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        my_parser.set_defaults(
            stage=list(self.stages),
            flaky_retry_attempts=5,
            flaky_retry_delay=1,
        )
        my_parser.add_argument(
            "--some-file",
            required=True,
            type=Path,
            help="Some file your users need to point to for the script "
            "to run.",
        )
        my_parser.add_argument(
            "--some-flag",
            action="store_true",
            help="Some flag your users can toggle on if they like.",
        )
        return my_parser

    def parse_args(self, argv: list[str]) -> None:
        # The base class saves the parsed arguments as `self.args`.
        super().parse_args(argv)

        # If you like, you may wish to transfer some subset of the added
        # arguments to instance attributes for convenience.
        self.flag = self.args.some_flag

        # You may also wish to do additional post-processing of certain
        # arguments, whether you save them as instance attributes or
        # not.
        self.args.some_file = self.args.some_file.resolve()

    def _run_pre_stage_actions(self) -> None:
        # You can extend the default implementation by calling it via
        # `super()` first.
        super()._run_pre_stage_actions()
        self.console.log("Checking to make sure it's safe to run a stage...")

    def _skip_stage(self) -> None:
        # You can override the default implementation if you don't like
        # it by simply omitting the `super()` call.
        self.console.log(
            f"You didn't tell me to run the '{self.current_stage}' stage."
        )

    def _end_stage(self) -> None:
        super()._end_stage()
        self.print_heading(f"Finished stage '{self.current_stage}'.")

    def _run_post_stage_actions(self) -> None:
        super()._run_post_stage_actions()
        self.console.log(
            "Checking to make sure all is well after running the stage..."
        )

    def _begin_stage_hello(self, heading: str) -> None:
        # You can use whatever `_begin_stage()` method already exists,
        # either whatever's been overridden or extended in the current
        # class, or whatever's provided by the base class, and then
        # extend it.
        self._begin_stage(heading)
        self.console.log("The first stage is underway...")

    def _end_stage_goodbye(self) -> None:
        # Or you can ignore whatever's been overridden/extended in the
        # current class, and fall back to what's provided by the base
        # class, and then extend it.
        super()._end_stage()
        self.print_heading(f"Finished the final stage:  {self.current_stage}")

        # You can also override things completely by omitting any `self`
        # or `super()` calls to the default method for the corresponding
        # phase, if you like.

    def print_script_execution_summary(
        self,
        extra_sections: Optional[dict[str, str]] = None,
    ) -> None:
        extras = {
            "Machine details": (
                f"hostname:  {socket.gethostname()}\n"
                f"platform:  {platform.platform()}"
            ),
        }
        if extra_sections is not None:
            extras |= extra_sections
        super().print_script_execution_summary(extra_sections=extras)

    def main(self, argv: list[str]) -> None:
        self.parse_args(argv)
        try:
            self.say_hello()
            self.try_error_prone_operation()
            self.say_goodbye()
        finally:
            self.print_script_execution_summary()


if __name__ == "__main__":
    my_script = MyScript({"hello", "flaky", "goodbye"})
    my_script.main(sys.argv[1:])
