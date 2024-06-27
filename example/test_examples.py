#!/usr/bin/env python3
"""Run all the examples and ensure their output is correct."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import subprocess
from pathlib import Path
from typing import List


def assert_output_in_order(stdout: str, output: List[str]) -> None:
    """
    Ensure the output appears in the correct order.

    Args:
        stdout:  The ``stdout`` of the command that was run.
        output:  The list of terms that should appear in the output in
            the given order.

    Raises:
        ValueError:  If any of the terms in the output list cannot be
            found.
    """
    index = 0
    for term in output:
        index = stdout.find(term, index) + len(term)


def test_ex_0_the_basics_help() -> None:
    example = Path(__file__).parent / "ex_0_the_basics.py"
    result = subprocess.run(
        [example, "--help"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "the ArgumentParser for the StagedScript base class.",
            "--stage {goodbye,hello}",
            "--goodbye-retry-attempts",
            "--goodbye-retry-delay",
            "--goodbye-retry-timeout",
            "--hello-retry-attempts",
            "--hello-retry-delay",
            "--hello-retry-timeout",
        ],
    )


def test_ex_0_the_basics() -> None:
    example = Path(__file__).parent / "ex_0_the_basics.py"
    result = subprocess.run(
        [example, "--stage", "hello"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Greeting the user",
            "Executing:  echo 'Hello World'",
            "`hello` stage duration",
            "Bidding farewell",
            "Skipping this stage",
            "`goodbye` stage duration",
            "Ran the following",
            "--hello-retry-attempts 0",
            "--hello-retry-delay 0",
            "--hello-retry-timeout 60",
            "--goodbye-retry-attempts 0",
            "--goodbye-retry-delay 0",
            "--goodbye-retry-timeout 60",
            "Commands executed",
            "Timing results",
            "Script result",
        ],
    )


def test_ex_1_removing_the_retry_arguments_help() -> None:
    example = Path(__file__).parent / "ex_1_removing_the_retry_arguments.py"
    result = subprocess.run(
        [example, "--help"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert "Demonstrate removing the retry arguments" in result.stdout
    for _ in [
        "--goodbye-retry-attempts",
        "--goodbye-retry-delay",
        "--goodbye-retry-timeout",
        "--hello-retry-attempts",
        "--hello-retry-delay",
        "--hello-retry-timeout",
    ]:
        assert _ not in result.stdout


def test_ex_1_removing_the_retry_arguments() -> None:
    example = Path(__file__).parent / "ex_1_removing_the_retry_arguments.py"
    result = subprocess.run(
        [example, "--stage", "hello"],
        capture_output=True,
        check=True,
        text=True,
    )
    for _ in [
        "--goodbye-retry-attempts",
        "--goodbye-retry-delay",
        "--goodbye-retry-timeout",
        "--hello-retry-attempts",
        "--hello-retry-delay",
        "--hello-retry-timeout",
    ]:
        assert _ not in result.stdout


def test_ex_2_running_certain_stages_by_default() -> None:
    example = (
        Path(__file__).parent / "ex_2_running_certain_stages_by_default.py"
    )
    result = subprocess.run(
        [example],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Greeting the user",
            "Executing:  echo 'Hello World'",
            "`hello` stage duration",
            "Bidding farewell",
            "Executing:  echo 'Goodbye World'",
            "`goodbye` stage duration",
        ],
    )


def test_ex_3_adding_arguments() -> None:
    example = Path(__file__).parent / "ex_3_adding_arguments.py"
    result = subprocess.run(
        [example, "--some-file", "foo.txt"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Greeting the user",
            "Executing:  echo 'Hello World'",
            "Processing file",
            "/foo.txt",
            "`hello` stage duration",
            "Bidding farewell",
            "Executing:  echo 'Goodbye World'",
            "Some flag was not set!",
            "`goodbye` stage duration",
        ],
    )


def test_ex_4_customizing_stage_behavior() -> None:
    example = Path(__file__).parent / "ex_4_customizing_stage_behavior.py"
    result = subprocess.run(
        [
            example,
            "--some-file",
            "foo.txt",
            "--some-flag",
            "--stage",
            "goodbye",
        ],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Checking to make sure it's safe to run a stage",
            "Greeting the user",
            "You didn't tell me to run the 'hello' stage",
            "`hello` stage duration",
            "Finished stage 'hello'",
            "Checking to make sure all is well after running",
            "Checking to make sure it's safe to run a stage",
            "Bidding farewell",
            "Executing:  echo 'Goodbye World'",
            "Some flag was set!",
            "`goodbye` stage duration",
            "Finished stage 'goodbye'",
            "Checking to make sure all is well after running",
        ],
    )


def test_ex_5_customizing_individual_stages() -> None:
    example = Path(__file__).parent / "ex_5_customizing_individual_stages.py"
    result = subprocess.run(
        [example, "--some-file", "foo.txt"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Checking to make sure it's safe to run a stage",
            "Greeting the user",
            "The first stage is underway",
            "Executing:  echo 'Hello World'",
            "Processing file",
            "/foo.txt",
            "`hello` stage duration",
            "Finished stage 'hello'",
            "Checking to make sure all is well after running",
            "Checking to make sure it's safe to run a stage",
            "Bidding farewell",
            "Executing:  echo 'Goodbye World'",
            "Some flag was not set!",
            "`goodbye` stage duration",
            "Finished the final stage:  goodbye",
            "Checking to make sure all is well after running",
        ],
    )


def test_ex_6_creating_retryable_stages_help() -> None:
    example = Path(__file__).parent / "ex_6_creating_retryable_stages.py"
    result = subprocess.run(
        [example, "--help"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "retry",
            "Additional options for retrying stages",
            "--flaky-retry-attempts",
            "--flaky-retry-delay",
            "--flaky-retry-timeout",
        ],
    )


def test_ex_6_creating_retryable_stages() -> None:
    example = Path(__file__).parent / "ex_6_creating_retryable_stages.py"
    result = subprocess.run(
        [example, "--some-file", "foo.txt"],
        capture_output=True,
        check=True,
        text=True,
    )
    flaky_output = [
        "Trying an error-prone operation",
        "Oh no!  Something went horribly wrong!",
        "`flaky` stage duration",
        "Finished stage 'flaky'",
        "Preparing to retry the 'flaky' stage",
        "RetryCallState",
    ]
    assert_output_in_order(
        result.stdout,
        [
            *flaky_output,
            *flaky_output,
            "Trying an error-prone operation",
            "Thank goodness, everything worked this time",
            "`flaky` stage duration",
            "Finished stage 'flaky'",
        ],
    )


def test_ex_6_creating_retryable_stages_no_retries() -> None:
    example = Path(__file__).parent / "ex_6_creating_retryable_stages.py"
    result = subprocess.run(
        [example, "--some-file", "foo.txt", "--flaky-retry-attempts", "0"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Trying an error-prone operation",
            "Oh no!  Something went horribly wrong!",
            "`flaky` stage duration",
            "Finished stage 'flaky'",
            "Checking to make sure all is well after running",
            "Checking to make sure it's safe to run a stage",
            "Bidding farewell",
            "Script result",
            "Failure",
        ],
    )


def test_ex_7_customizing_the_summary() -> None:
    example = Path(__file__).parent / "ex_7_customizing_the_summary.py"
    result = subprocess.run(
        [example, "--some-file", "foo.txt", "--stage", "hello"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert_output_in_order(
        result.stdout,
        [
            "Script result",
            "Success",
            "Machine details",
            "hostname",
            "platform",
        ],
    )
