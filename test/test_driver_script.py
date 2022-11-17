#!/usr/bin/env python3
from datetime import datetime, timedelta

from rich.console import Console
from python.driver_script.driver_script.driver_script import DriverScript
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
    assert stage_name in ds.durations
    assert "duration:" in captured.out
    assert str(ds.durations[stage_name]) in captured.out


def test__skip_stage(ds: DriverScript, capsys: pytest.CaptureFixture) -> None:
    ds._skip_stage()
    captured = capsys.readouterr()
    assert "Skipping this stage." in captured.out


def test_get_timing_report(
    ds: DriverScript,
    capsys: pytest.CaptureFixture
) -> None:
    ds.durations = {
        "first": timedelta(hours=1, minutes=2, seconds=3, microseconds=4),
        "second": timedelta(hours=4, minutes=3, seconds=2, microseconds=1)
    }  # yapf: disable
    ds.console.print(ds.get_timing_report())
    captured = capsys.readouterr()
    for stage in ds.durations:
        assert stage in captured.out
    for duration in ds.durations.values():
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
