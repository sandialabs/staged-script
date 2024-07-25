"""Unit tests for ``staged-script``."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

import shlex
from datetime import datetime, timedelta, timezone
from subprocess import CompletedProcess
from typing import Dict, Optional
from unittest.mock import MagicMock, patch

import pytest
from rich.console import Console

from staged_script import StagedScript, StageDuration


@pytest.fixture()
def script() -> StagedScript:
    """Create a :class:`StagedScript` object to be used by tests."""
    staged_script = StagedScript(set())
    staged_script.console = Console(log_time=False, log_path=False)
    return staged_script


def test_print_dry_run_message(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`print_dry_run_message` method."""
    message = "dry run message"
    expected = f"DRY-RUN MODE:  {message}"
    script.print_dry_run_message(message)
    captured = capsys.readouterr()
    assert expected in captured.out


def test__validate_stage_name() -> None:
    """Test the :func:`validate_stage_name` method."""
    StagedScript._validate_stage_name("valid")


@pytest.mark.parametrize(
    "stage_name", ["Uppercase", "spa ces", "hyphen-ated", "under_scores"]
)
def test__validate_stage_name_raises(stage_name: str) -> None:
    """Ensure :func:`validate_stage_name` raises an exception when needed."""
    with pytest.raises(
        ValueError,
        match=f"'{stage_name}' must contain only lowercase letters",
    ):
        StagedScript._validate_stage_name(stage_name)


def test__begin_stage(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`_begin_stage` method."""
    message = "begin stage"
    script._begin_stage(message)
    captured = capsys.readouterr()
    assert message in captured.out
    assert script.stage_start_time is not None


def test__end_stage(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`_end_stage` method."""
    stage_name = "test"
    script.current_stage = stage_name
    script.stage_start_time = datetime.now(tz=timezone.utc)
    script._end_stage()
    captured = capsys.readouterr()
    assert stage_name in [_.stage for _ in script.durations]
    assert "duration:" in captured.out
    assert str(script.durations[-1].duration) in captured.out


def test__skip_stage(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`_skip_stage` method."""
    script._skip_stage()
    captured = capsys.readouterr()
    assert "Skipping this stage." in captured.out


@pytest.mark.parametrize("retry_attempts", [0, 5])
@patch("tenacity.Retrying")
def test__handle_stage_retry_error(
    mock_Retrying: MagicMock,
    retry_attempts: int,
    script: StagedScript,
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the :func:`_handle_stage_retry_error` method."""
    script.current_stage = "test"
    script.retry_attempts["test"] = retry_attempts
    retry = mock_Retrying()
    retry.statistics = {
        "delay_since_first_attempt": 1234,
        "attempt_number": retry_attempts,
    }
    script._handle_stage_retry_error(retry)
    captured = capsys.readouterr()
    if retry_attempts == 0:
        assert captured.out == ""
    else:
        for text in [
            "Abandoning retrying the 'test' stage.",
            "Total attempts:",
            "5.",
            "Total time:",
            "0:20:34.",
        ]:
            assert text in captured.out


@patch("tenacity.RetryCallState")
def test__prepare_to_retry_stage(
    mock_RetryCallState: MagicMock,
    script: StagedScript,
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the :func:`_prepare_to_retry_stage` method."""
    script.current_stage = "test"
    retry_state = mock_RetryCallState()
    retry_state.__repr__ = lambda self: "mock_RetryCallState.__repr__"
    script._prepare_to_retry_stage(retry_state)
    captured = capsys.readouterr()
    for text in [
        "Preparing to retry the 'test' stage...",
        "mock_RetryCallState.__repr__",
    ]:
        assert text in captured.out


def test__get_timing_report(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`_get_timing_report` method."""
    script.durations = [
        StageDuration(
            "first", timedelta(hours=1, minutes=2, seconds=3, microseconds=4)
        ),
        StageDuration(
            "second", timedelta(hours=4, minutes=3, seconds=2, microseconds=1)
        ),
    ]
    script.console.print(script._get_timing_report())
    captured = capsys.readouterr()
    for stage in [_.stage for _ in script.durations]:
        assert stage in captured.out
    for duration in [_.duration for _ in script.durations]:
        assert str(duration) in captured.out
    assert "Total" in captured.out


@pytest.mark.parametrize(
    ("command", "expected"),
    [
        ("command --foo", "command \\\n    --foo"),
        ("command --foo bar baz", "command \\\n    --foo bar \\\n    baz"),
        ("command foo bar baz", "command \\\n    foo \\\n    bar \\\n    baz"),
        ("command --foo --bar baz", "command \\\n    --foo \\\n    --bar baz"),
        ("command --foo 'bar baz'", "command \\\n    --foo 'bar baz'"),
        ("command -f bar", "command \\\n    -f \\\n    bar"),
        ("command --foo -b", "command \\\n    --foo \\\n    -b"),
    ],
)
def test_pretty_print_command(
    command: str, expected: str, script: StagedScript
) -> None:
    """Test the :func:`pretty_print_command` method."""
    assert script.pretty_print_command(command) == expected


def test_parse_args(script: StagedScript) -> None:
    """Test the :func:`parse_args` method."""
    script.stages = {"first", "second", "third"}
    script.parse_args(shlex.split("--dry-run --stage first third"))
    assert script.dry_run is True
    assert script.stages_to_run == {"first", "third"}


@pytest.mark.parametrize("print_commands", [True, False])
@patch("subprocess.run")
def test_run(
    mock_run: MagicMock,
    print_commands: bool,  # noqa: FBT001
    script: StagedScript,
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the :func:`run` method."""
    command = "echo 'hello world'"
    mock_run.return_value = CompletedProcess(args=command, returncode=0)
    script.print_commands = print_commands
    script.run(command)
    captured = capsys.readouterr()
    if print_commands:
        assert f"Executing:  {command}" in captured.out
    else:
        assert f"Executing:  {command}" not in captured.out
    assert command in script.commands_executed


@patch("subprocess.run")
def test_run_override_print_commands(
    mock_run: MagicMock, script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Ensure :func:`run` prints the command executed when appropriate."""
    command = "echo 'hello world'"
    mock_run.return_value = CompletedProcess(args=command, returncode=0)
    script.run(command, print_command=False)
    captured = capsys.readouterr()
    assert f"Executing:  {command}" not in captured.out
    script.print_commands = False
    script.run(command, print_command=True)
    captured = capsys.readouterr()
    assert f"Executing:  {command}" in captured.out


def test_run_dry_run(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`run` method in dry-run mode."""
    command = "echo 'dry-run mode'"
    script.dry_run = True
    script.run(command)
    captured = capsys.readouterr()
    for _ in ["The command executed would be", command]:
        assert _ in captured.out


@pytest.mark.parametrize("script_success", [True, False])
@pytest.mark.parametrize(
    "extras",
    [
        {
            "More information": "Additional details.",
            "Another section": "With still more information.",
        },
        None,
    ],
)
@patch(
    "reverse_argparse.ReverseArgumentParser."
    "get_pretty_command_line_invocation"
)
def test_print_script_execution_summary(
    mock_get_pretty_command_line_invocation: MagicMock,
    extras: Optional[Dict[str, str]],
    script_success: bool,  # noqa: FBT001
    script: StagedScript,
    capsys: pytest.CaptureFixture,
) -> None:
    """Test the :func:`print_script_execution_summary` method."""
    mock_get_pretty_command_line_invocation.return_value = (
        "command line invocation"
    )
    script.durations = [
        StageDuration(
            "first", timedelta(hours=1, minutes=2, seconds=3, microseconds=4)
        ),
        StageDuration(
            "second", timedelta(hours=4, minutes=3, seconds=2, microseconds=1)
        ),
    ]
    script.commands_executed = ["foo", "bar", "baz"]
    script.script_success = script_success
    if extras is None:
        script.print_script_execution_summary()
    else:
        script.print_script_execution_summary(extra_sections=extras)
    captured = capsys.readouterr()
    headings = [
        "Ran the following",
        "Commands executed",
        "Timing results",
        "Script result",
    ]
    details = (
        [mock_get_pretty_command_line_invocation.return_value]
        + script.commands_executed
        + [_.stage for _ in script.durations]
        + [str(_.duration) for _ in script.durations]
        + ["Success" if script_success else "Failure"]
    )
    if extras is not None:
        headings += list(extras.keys())
        details += list(extras.values())
    for item in headings + details:
        assert item in captured.out


def test_raise_parser_error(
    script: StagedScript, capsys: pytest.CaptureFixture
) -> None:
    """Test the :func:`raise_parser_error` method."""
    error_message = (
        "This is a lengthy error message explaining what exactly went wrong, "
        "where, and why.  It's so long it should get wrapped over multiple "
        "lines."
    )
    with pytest.raises(SystemExit):
        script.raise_parser_error(error_message)
    captured = capsys.readouterr()
    expected = [*error_message.split(), "usage:", "--dry-run", "--stage"]
    for term in expected:
        assert term in captured.out
