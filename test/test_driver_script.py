#!/usr/bin/env python3
import shlex
from datetime import datetime, timedelta
from subprocess import CompletedProcess
from unittest.mock import MagicMock, patch

import pytest
from rich.console import Console

from python.driver_script.driver_script.driver_script import (
    DriverScript,
    StageDuration
)


@pytest.fixture()
def ds() -> DriverScript:
    driver_script = DriverScript()
    driver_script.console = Console(log_time=False, log_path=False)
    return driver_script


def test_print_dry_run_message(
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    message = "dry run message"
    expected = f"DRY-RUN MODE:  {message}"
    ds.print_dry_run_message(message)
    captured = capsys.readouterr()
    assert expected in captured.out


def test__add_stage(capsys: pytest.CaptureFixture) -> None:
    stages_before = DriverScript.stages
    DriverScript.stages = []
    DriverScript._add_stage("first")
    DriverScript._add_stage("second")
    DriverScript._add_stage("first")
    assert DriverScript.stages == ["first", "second"]
    captured = capsys.readouterr()
    assert "you're redefining the 'first' stage" in captured.out
    DriverScript.stages = stages_before


@pytest.mark.parametrize(
    "stage_name",
    ["Uppercase", "spa ces", "hyphen-ated", "under_scores"]
)  # yapf: disable
def test__add_stage_raises(stage_name: str) -> None:
    with pytest.raises(ValueError) as e:
        DriverScript._add_stage(stage_name)
    msg = e.value.args[0]
    assert f"'{stage_name}' must contain only lowercase letters" in msg


def test__begin_stage(ds: DriverScript, capsys: pytest.CaptureFixture) -> None:
    message = "begin stage"
    ds._begin_stage(message)
    captured = capsys.readouterr()
    assert message in captured.out
    assert ds.stage_start_time is not None


def test__end_stage(ds: DriverScript, capsys: pytest.CaptureFixture) -> None:
    stage_name = "test"
    ds.current_stage = stage_name
    ds.stage_start_time = datetime.now()
    ds._end_stage()
    captured = capsys.readouterr()
    assert stage_name in [_.stage for _ in ds.durations]
    assert "duration:" in captured.out
    assert str(ds.durations[-1].duration) in captured.out


def test__skip_stage(ds: DriverScript, capsys: pytest.CaptureFixture) -> None:
    ds._skip_stage()
    captured = capsys.readouterr()
    assert "Skipping this stage." in captured.out


@pytest.mark.parametrize("retry_attempts", [0, 5])
@patch("tenacity.Retrying")
def test__handle_stage_retry_error(
    mock_Retrying: MagicMock,
    retry_attempts: int,
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    ds.current_stage = "test"
    ds.test_retry_attempts = retry_attempts
    retry = mock_Retrying()
    retry.statistics = {
        "delay_since_first_attempt": 1234,
        "attempt_number": retry_attempts
    }
    ds._handle_stage_retry_error(retry)
    captured = capsys.readouterr()
    if retry_attempts == 0:
        assert captured.out == ""
    else:
        for text in [
            "Abandoning retrying the 'test' stage.",
            "Total attempts:",
            "5.",
            "Total time:",
            "0:20:34."
        ]:
            assert text in captured.out


@patch("tenacity.RetryCallState")
def test__prepare_to_retry_stage(
    mock_RetryCallState: MagicMock,
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    ds.current_stage = "test"
    retry_state = mock_RetryCallState()
    retry_state.__repr__ = lambda self: "mock_RetryCallState.__repr__"
    ds._prepare_to_retry_stage(retry_state)
    captured = capsys.readouterr()
    for text in [
        "Preparing to retry the 'test' stage...",
        "mock_RetryCallState.__repr__"
    ]:
        assert text in captured.out


def test_get_timing_report(
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    ds.durations = [
        StageDuration(
            "first",
            timedelta(hours=1, minutes=2, seconds=3, microseconds=4)
        ),
        StageDuration(
            "second",
            timedelta(hours=4, minutes=3, seconds=2, microseconds=1)
        )
    ]  # yapf: disable
    ds.console.print(ds.get_timing_report())
    captured = capsys.readouterr()
    for stage in [_.stage for _ in ds.durations]:
        assert stage in captured.out
    for duration in [_.duration for _ in ds.durations]:
        assert str(duration) in captured.out
    assert "Total" in captured.out


@pytest.mark.parametrize(
    "command, expected",
    [("command --foo",
      "command \\\n    --foo"),
     ("command --foo bar baz",
      "command \\\n    --foo bar \\\n    baz"),
     ("command foo bar baz",
      "command \\\n    foo \\\n    bar \\\n    baz"),
     ("command --foo --bar baz",
      "command \\\n    --foo \\\n    --bar baz"),
     ("command foo bar baz",
      "command \\\n    foo \\\n    bar \\\n    baz"),
     ("command --foo 'bar baz'",
      "command \\\n    --foo 'bar baz'"),
     ("command -f bar",
      "command \\\n    -f \\\n    bar"),
     ("command --foo -b",
      "command \\\n    --foo \\\n    -b")]
)
def test_pretty_print_command(
    command: str,
    expected: str,
    ds: DriverScript
) -> None:
    assert ds.pretty_print_command(command) == expected


def test_parse_args(ds: DriverScript) -> None:
    ds.stages = ["first", "second", "third"]
    ds.parse_args(shlex.split("--dry-run --stage first third"))
    assert ds.dry_run is True
    assert ds.stages_to_run == {"first", "third"}


@pytest.mark.parametrize("print_commands", [True, False])
@patch("subprocess.run")
def test_run(
    mock_run: MagicMock,
    print_commands: bool,
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    command = "echo 'hello world'"
    mock_run.return_value = CompletedProcess(args=command, returncode=0)
    ds.print_commands = print_commands
    ds.run(command)
    captured = capsys.readouterr()
    if print_commands:
        assert f"Executing:  {command}" in captured.out
    else:
        assert f"Executing:  {command}" not in captured.out
    assert command in ds.commands_executed


@patch("subprocess.run")
def test_run_override_print_commands(
    mock_run: MagicMock,
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    command = "echo 'hello world'"
    mock_run.return_value = CompletedProcess(args=command, returncode=0)
    ds.run(command, print_command=False)
    captured = capsys.readouterr()
    assert f"Executing:  {command}" not in captured.out
    ds.print_commands = False
    ds.run(command, print_command=True)
    captured = capsys.readouterr()
    assert f"Executing:  {command}" in captured.out


@pytest.mark.parametrize("script_success", [True, False])
@pytest.mark.parametrize(
    "extras",
    [
        {
            "More information": "Additional details.",
            "Another section": "With still more information."
        },
        None
    ]
)
@patch(
    "reverse_argparse.ReverseArgumentParser."
    "get_pretty_command_line_invocation"
)
def test_print_script_execution_summary(
    mock_get_pretty_command_line_invocation: MagicMock,
    extras: dict[str, str] | None,
    script_success: bool,
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    mock_get_pretty_command_line_invocation.return_value = (
        "command line invocation"
    )
    ds.durations = [
        StageDuration(
            "first",
            timedelta(hours=1, minutes=2, seconds=3, microseconds=4)
        ),
        StageDuration(
            "second",
            timedelta(hours=4, minutes=3, seconds=2, microseconds=1)
        )
    ]  # yapf: disable
    ds.commands_executed = ["foo", "bar", "baz"]
    ds.script_success = script_success
    if extras is None:
        ds.print_script_execution_summary()
    else:
        ds.print_script_execution_summary(extra_sections=extras)
    captured = capsys.readouterr()
    headings = [
        "Ran the following",
        "Commands executed",
        "Timing results",
        "Script result"
    ]
    details = (
        [mock_get_pretty_command_line_invocation.return_value]
        + ds.commands_executed
        + [_.stage for _ in ds.durations]
        + [str(_.duration) for _ in ds.durations]
        + ["Success" if script_success else "Failure"]
    )  # yapf: disable
    if extras is not None:
        headings += list(extras.keys())
        details += list(extras.values())
    for item in headings + details:
        assert item in captured.out
