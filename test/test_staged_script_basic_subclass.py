"""Integration tests for a basic ``StagedScript`` use case."""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

from typing import Set

import pytest
from rich.console import Console

from staged_script import StagedScript


class MyBasicScript(StagedScript):
    """
    A basic staged script.

    Stage methods are defined, but no fancy phase customizations are
    made.
    """

    @StagedScript.stage("good", "Stage that executes correctly")
    def run_good_stage(self) -> None:
        """A simple stage that runs as expected."""
        print("inside 'run_good_stage' function")

    @StagedScript.stage("bad", "Stage that throws an exception")
    def run_bad_stage(self, *, error: bool) -> None:
        """
        A simple stage that might run into an error.

        Args:
            error:  Whether an error should occur.
        """
        if error:
            message = "Something went wrong."
            raise RuntimeError(message)
        print("Got past error.")


@pytest.fixture
def script() -> MyBasicScript:
    """Create a :class:`MyBasicScript` object to be used by tests."""
    my_basic_script = MyBasicScript({"good", "bad"})
    my_basic_script.console = Console(log_time=False, log_path=False)
    return my_basic_script


@pytest.mark.parametrize("stages_to_run", [{"good"}, set()])
def test_good_stage(
    stages_to_run: Set[str],
    script: MyBasicScript,
    capsys: pytest.CaptureFixture,
) -> None:
    """Ensure the good stage runs to completion."""
    script.parse_args([])
    script.stages_to_run = stages_to_run
    script.run_good_stage()
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
    error: bool,  # noqa: FBT001
    script: MyBasicScript,
    capsys: pytest.CaptureFixture,
) -> None:
    """
    Ensure the bad stage runs as expected.

    If there's no error, it runs to completion; otherwise it bugs out in
    the stage body, but still runs the end-stage actions.
    """
    script.parse_args([])
    script.stages_to_run = {"bad"}
    if error:
        with pytest.raises(RuntimeError) as e:
            script.run_bad_stage(error=error)
        msg = e.value.args[0]
        assert "Something went wrong." in msg
    else:
        script.run_bad_stage(error=error)
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
def test_parser_retry_options(stage: str, script: MyBasicScript) -> None:
    """Ensure the stage retry options are present."""
    help_text = script.parser.format_help()
    assert f"--{stage}-retry-attempts" in help_text
    assert f"--{stage}-retry-delay" in help_text
    assert f"--{stage}-retry-timeout" in help_text
