#!/usr/bin/env python3
"""A staged script without retry arguments."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import argparse
import functools
import sys
from argparse import ArgumentParser
from typing import List

from staged_script import StagedScript


class MyScript(StagedScript):
    @StagedScript.stage("hello", "Greeting the user")
    def say_hello(self) -> None:
        self.run("echo 'Hello World'", shell=True)

    @StagedScript.stage("goodbye", "Bidding farewell")
    def say_goodbye(self) -> None:
        self.run("echo 'Goodbye World'", shell=True)

    @functools.cached_property
    def parser(self) -> ArgumentParser:
        my_parser = super().parser
        my_parser.description = "Demonstrate removing the retry arguments."
        self.retry_arg_group.title = argparse.SUPPRESS
        self.retry_arg_group.description = argparse.SUPPRESS
        self.retry_attempts_arg["hello"].help = argparse.SUPPRESS
        self.retry_delay_arg["hello"].help = argparse.SUPPRESS
        self.retry_timeout_arg["hello"].help = argparse.SUPPRESS
        self.retry_attempts_arg["goodbye"].help = argparse.SUPPRESS
        self.retry_delay_arg["goodbye"].help = argparse.SUPPRESS
        self.retry_timeout_arg["goodbye"].help = argparse.SUPPRESS
        return my_parser

    def main(self, argv: List[str]) -> None:
        self.parse_args(argv)
        try:
            self.say_hello()
            self.say_goodbye()
        finally:
            self.print_script_execution_summary()


if __name__ == "__main__":
    my_script = MyScript({"hello", "goodbye"})
    my_script.main(sys.argv[1:])
