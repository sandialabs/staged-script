#!/usr/bin/env python3
from python.staged_script.staged_script.staged_script import StagedScript


class MyScript(StagedScript):
    ...


def test_parser_registered_stages() -> None:
    stages = {"one", "two", "three"}
    script = MyScript(stages)
    help_text = script.parser.format_help()
    expected = ["Additional options for retrying stages"]
    for stage in stages:
        expected += [
            f"{stage}-retry-attempts",
            f"{stage}-retry-delay",
            f"{stage}-retry-timeout"
        ]
    for text in expected:
        assert text in help_text


def test_parser_no_registered_stages() -> None:
    script = MyScript(set())
    help_text = script.parser.format_help()
    for text in [
        "Options for retrying stages"
        "-retry-attempts",
        "-retry-delay",
        "-retry-timeout",
    ]:
        assert text not in help_text
