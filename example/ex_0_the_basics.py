#!/usr/bin/env python3
"""A very basic staged script."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import sys

from staged_script import StagedScript


class MyScript(StagedScript):
    @StagedScript.stage("hello", "Greeting the user")
    def say_hello(self) -> None:
        self.run("echo 'Hello World'", shell=True)

    @StagedScript.stage("goodbye", "Bidding farewell")
    def say_goodbye(self) -> None:
        self.run("echo 'Goodbye World'", shell=True)

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
