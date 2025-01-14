"""Integration tests for retry options."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

from staged_script import StagedScript


class MyScript(StagedScript):
    """A basic staged script to test the retry options in the help text."""


def test_parser_registered_stages() -> None:
    """Ensure retry options are in the help text for all registered stages."""
    stages = {"one", "two", "three"}
    script = MyScript(stages)
    help_text = script.parser.format_help()
    expected = ["Additional options for retrying stages"]
    for stage in stages:
        expected += [
            f"{stage}-retry-attempts",
            f"{stage}-retry-delay",
            f"{stage}-retry-timeout",
        ]
    for text in expected:
        assert text in help_text


def test_parser_no_registered_stages() -> None:
    """Ensure retry options are absent when no stages are registered."""
    script = MyScript(set())
    help_text = script.parser.format_help()
    for text in [
        "Options for retrying stages",
        "-retry-attempts",
        "-retry-delay",
        "-retry-timeout",
    ]:
        assert text not in help_text
