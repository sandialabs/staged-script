#!/usr/bin/env python3
"""A staged script with phases customized per stage."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import argparse
import functools
import sys
from argparse import ArgumentParser
from pathlib import Path

from staged_script import StagedScript


class MyScript(StagedScript):
    @StagedScript.stage("hello", "Greeting the user")
    def say_hello(self) -> None:
        self.run("echo 'Hello World'", shell=True)
        self.console.log(f"Processing file:  {self.args.some_file}")

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
        self.retry_arg_group.title = argparse.SUPPRESS
        self.retry_arg_group.description = argparse.SUPPRESS
        self.retry_attempts_arg["hello"].help = argparse.SUPPRESS
        self.retry_delay_arg["hello"].help = argparse.SUPPRESS
        self.retry_timeout_arg["hello"].help = argparse.SUPPRESS
        self.retry_attempts_arg["goodbye"].help = argparse.SUPPRESS
        self.retry_delay_arg["goodbye"].help = argparse.SUPPRESS
        self.retry_timeout_arg["goodbye"].help = argparse.SUPPRESS
        my_parser.set_defaults(stage=list(self.stages))
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

    def main(self, argv: list[str]) -> None:
        self.parse_args(argv)
        try:
            self.say_hello()
            self.say_goodbye()
        finally:
            self.print_script_execution_summary()


if __name__ == "__main__":
    my_script = MyScript({"hello", "goodbye"})
    my_script.main(sys.argv[1:])
