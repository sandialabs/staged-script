#!/usr/bin/env python3
import shlex
from datetime import datetime, timedelta
from subprocess import CompletedProcess
from unittest.mock import MagicMock, patch

from rich.console import Console
from python.driver_script.driver_script.driver_script import (
    DriverScript,
    StageDuration
)
import pytest


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


def test__begin_stage(ds: DriverScript, capsys: pytest.CaptureFixture) -> None:
    stage_name = "test"
    message = "begin stage"
    ds._begin_stage(stage_name, message)
    captured = capsys.readouterr()
    assert message in captured.out
    assert ds.current_stage == stage_name
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


@patch("subprocess.run")
def test_run(
    mock_run: MagicMock,
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    command = "echo 'hello world'"
    mock_run.return_value = CompletedProcess(args=command, returncode=0)
    ds.run(command)
    captured = capsys.readouterr()
    assert all(_ in captured.out for _ in ["Executing", command])
    assert command in ds.commands_executed


@patch(
    "reverse_argparse.ReverseArgumentParser."
    "get_pretty_command_line_invocation"
)
def test_print_script_execution_summary(
    mock_get_pretty_command_line_invocation: MagicMock,
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
    extras = {
        "More information": "Additional details.",
        "Another section": "With still more information."
    }
    ds.print_script_execution_summary(extra_sections=extras)
    captured = capsys.readouterr()
    headings = (
        ["Ran the following", "Commands executed", "Timing results"]
        + list(extras.keys())
    )  # yapf: disable
    details = (
        [mock_get_pretty_command_line_invocation.return_value]
        + ds.commands_executed
        + [_.stage for _ in ds.durations]
        + [str(_.duration) for _ in ds.durations]
        + list(extras.values())
    )  # yapf: disable
    for item in headings + details:
        assert item in captured.out
