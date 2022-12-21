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

    def _skip_stage(self) -> None:
        print("inside '_skip_stage' function")

    def _end_stage(self) -> None:
        print("inside '_end_stage' function")

    def _run_post_stage_actions(self) -> None:
        print("inside '_run_post_stage_actions' function")


def check_phase(custom: bool, method_name: str, output: str) -> None:
    if custom:
        assert f"inside '{method_name}_test' function" in output
    else:
        assert f"inside '{method_name}' function" in output


@pytest.mark.parametrize("custom_post_stage", [True, False])
@pytest.mark.parametrize("custom_end_stage", [True, False])
@pytest.mark.parametrize("custom_skip_stage", [True, False])
@pytest.mark.parametrize("custom_begin_stage", [True, False])
@pytest.mark.parametrize("custom_pre_stage", [True, False])
@pytest.mark.parametrize("stages_to_run", [{"test"}, set()])
def test_stage(
    stages_to_run: set[str],
    custom_pre_stage: bool,
    custom_begin_stage: bool,
    custom_skip_stage: bool,
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
    if custom_skip_stage:
        script._skip_stage_test = (
            lambda: print("inside '_skip_stage_test' function")
        )
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
    check_phase(custom_pre_stage, "_run_pre_stage_actions", captured.out)
    check_phase(custom_begin_stage, "_begin_stage", captured.out)
    if "test" in stages_to_run:
        assert "inside 'run_test' function" in captured.out
    else:
        check_phase(custom_skip_stage, "_skip_stage", captured.out)
    check_phase(custom_end_stage, "_end_stage", captured.out)
    check_phase(custom_post_stage, "_run_post_stage_actions", captured.out)
