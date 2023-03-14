#!/usr/bin/env python3
import pytest
from rich.console import Console

from python.driver_script.driver_script.driver_script import DriverScript


class MyBasicScript(DriverScript):

    @DriverScript.stage("good", "Stage that executes correctly")
    def run_good_stage(self) -> None:
        print("inside 'run_good_stage' function")

    @DriverScript.stage("bad", "Stage that throws an exception")
    def run_bad_stage(self, error: bool) -> None:
        if error:
            raise RuntimeError("Something went wrong.")
        print("Got past error.")


@pytest.fixture()
def mbs() -> MyBasicScript:
    my_basic_script = MyBasicScript({"good", "bad"})
    my_basic_script.console = Console(log_time=False, log_path=False)
    return my_basic_script


@pytest.mark.parametrize("stages_to_run", [{"good"}, set()])
def test_good_stage(
    stages_to_run: set[str],
    mbs: MyBasicScript,
    capsys: pytest.CaptureFixture
) -> None:
    mbs.parse_args([])
    mbs.stages_to_run = stages_to_run
    mbs.run_good_stage()
    captured = capsys.readouterr()

    # Ensure `_begin_stage()` is called.
    assert "Stage that executes correctly" in captured.out

    # Ensure the stage runs or is skipped.
    if "good" in stages_to_run:
        assert "inside 'run_good_stage' function" in captured.out
    else:
        assert "Skipping this stage." in captured.out

    # Ensure `_end_stage()` is called.
    assert "duration:" in captured.out


@pytest.mark.parametrize("error", [True, False])
def test_bad_stage(
    error: bool,
    mbs: MyBasicScript,
    capsys: pytest.CaptureFixture
) -> None:
    mbs.parse_args([])
    mbs.stages_to_run = {"bad"}
    if error:
        with pytest.raises(RuntimeError) as e:
            mbs.run_bad_stage(error)
        msg = e.value.args[0]
        assert "Something went wrong." in msg
    else:
        mbs.run_bad_stage(error)
    captured = capsys.readouterr()

    # Ensure `_begin_stage()` is called.
    assert "Stage that throws an exception" in captured.out

    # Ensure exceptions in the stage are handled appropriately.
    if error:
        assert "Got past error." not in captured.out
    else:
        assert "Got past error." in captured.out

    # Ensure `_end_stage()` is called, regardless of exceptions.
    assert "duration:" in captured.out


@pytest.mark.parametrize("stage", ["good", "bad"])
def test_parser_retry_options(stage: str, mbs: MyBasicScript) -> None:
    help_text = mbs.parser.format_help()
    assert f"--{stage}-retry-attempts" in help_text
    assert f"--{stage}-retry-delay" in help_text
    assert f"--{stage}-retry-timeout" in help_text
