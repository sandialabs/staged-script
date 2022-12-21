#!/usr/bin/env python3
from python.driver_script.driver_script.driver_script import DriverScript
import pytest


class MyAdvancedScript(DriverScript):

    @DriverScript.stage("test", "Test stage")
    def run_test(self) -> None:
        print("inside 'run_test' function")

    def _run_pre_stage_actions(self) -> None:
        print("inside '_run_pre_stage_actions' function")

    def _begin_stage(self, stage_name: str, heading: str) -> None:
        print("inside '_begin_stage' function")

    def _end_stage(self) -> None:
        print("inside '_end_stage' function")

    def _run_post_stage_actions(self) -> None:
        print("inside '_run_post_stage_actions' function")


@pytest.mark.parametrize("custom_post_stage", [True, False])
@pytest.mark.parametrize("custom_end_stage", [True, False])
@pytest.mark.parametrize("custom_begin_stage", [True, False])
@pytest.mark.parametrize("custom_pre_stage", [True, False])
@pytest.mark.parametrize("stages_to_run", [{"test"}, set()])
def test_stage(
    stages_to_run: set[str],
    custom_pre_stage: bool,
    custom_begin_stage: bool,
    custom_end_stage: bool,
    custom_post_stage: bool,
    capsys: pytest.CaptureFixture
) -> None:
    script = MyAdvancedScript()
    script.stages_to_run = stages_to_run
    if custom_pre_stage:
        script._run_pre_stage_actions_test = (
            lambda: print("inside '_run_pre_stage_actions_test' function")
        )
    if custom_begin_stage:
        script._begin_stage_test = (
            lambda stage_name, heading:
                print("inside '_begin_stage_test' function")
        )  # yapf: disable
    if custom_end_stage:
        script._end_stage_test = (
            lambda: print("inside '_end_stage_test' function")
        )
    if custom_post_stage:
        script._run_post_stage_actions_test = (
            lambda: print("inside '_run_post_stage_actions_test' function")
        )
    script.run_test()
    captured = capsys.readouterr()

    # Ensure pre-stage actions were run.
    if custom_pre_stage:
        assert "inside '_run_pre_stage_actions_test' function" in captured.out
    else:
        assert "inside '_run_pre_stage_actions' function" in captured.out

    # Ensure begin stage actions were run.
    if custom_begin_stage:
        assert "inside '_begin_stage_test' function" in captured.out
    else:
        assert "inside '_begin_stage' function" in captured.out

    # Ensure the stage runs or is skipped.
    if "test" in stages_to_run:
        assert "inside 'run_test' function" in captured.out
    else:
        assert "Skipping this stage." in captured.out

    # Ensure end stage actions were run.
    if custom_end_stage:
        assert "inside '_end_stage_test' function" in captured.out
    else:
        assert "inside '_end_stage' function" in captured.out

    # Ensure post-stage actions were run.
    if custom_post_stage:
        assert "inside '_run_post_stage_actions_test' function" in captured.out
    else:
        assert "inside '_run_post_stage_actions' function" in captured.out
