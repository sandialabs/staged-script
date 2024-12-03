#!/usr/bin/env python3
"""A staged script with additional arguments."""

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
        self.hello_retry_attempts_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.hello_retry_delay_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.hello_retry_timeout_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.goodbye_retry_attempts_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.goodbye_retry_delay_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
        self.goodbye_retry_timeout_arg.help = argparse.SUPPRESS  # type: ignore[attr-defined]
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
