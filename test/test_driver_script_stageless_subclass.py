#!/usr/bin/env python3
from python.driver_script.driver_script.driver_script import DriverScript


class MyStagelessScript(DriverScript):

    def no_stages(self) -> None:
        print("Note that this subclass defines no 'stage's.")


# Force the correct `stages` to get around a problem with how `pytest`
# runs against all these files at once in CI.
MyStagelessScript.stages = []


def test_parser() -> None:
    script = MyStagelessScript()
    script.stages = []
    print(f"{script.stages=}")
    print(f"{MyStagelessScript.stages=}")
    print(f"{DriverScript.stages=}")
    help_text = script.parser.format_help()
    for text in [
        "Options for retrying stages"
        "-retry-attempts",
        "-retry-delay",
        "-retry-timeout",
    ]:
        assert text not in help_text
