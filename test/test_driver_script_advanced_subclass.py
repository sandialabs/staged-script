#!/usr/bin/env python3
import shlex

from tenacity import RetryCallState, Retrying, TryAgain

from python.driver_script.driver_script.driver_script import DriverScript
import pytest


class MyAdvancedScript(DriverScript):

    @DriverScript.stage("test", "Test stage")
    def run_test(self, retry: bool = False) -> None:
        print("inside 'run_test' function")
        if retry:
            raise TryAgain("Stage failed; retrying...")

    def _run_pre_stage_actions(self) -> None:
        print("inside '_run_pre_stage_actions' function")

    def _begin_stage(self, heading: str) -> None:
        print("inside '_begin_stage' function")

    def _skip_stage(self) -> None:
        print("inside '_skip_stage' function")

    def _end_stage(self) -> None:
        print("inside '_end_stage' function")

    def _run_post_stage_actions(self) -> None:
        print("inside '_run_post_stage_actions' function")

    def _handle_stage_retry_error(
        self,
        retry: Retrying
    ) -> None:
        print("inside '_handle_stage_retry_error' function")

    def _prepare_to_retry_stage(self, retry_state: RetryCallState) -> None:
        print("inside '_prepare_to_retry_stage' function")


# Force the correct `stages` to get around a problem with how `pytest`
# runs against all these files at once in CI.
MyAdvancedScript.stages = ["test"]


def ensure_phase_comes_next(
    method_name: str,
    output: str,
    custom: bool = False,
    start: int = 0
) -> int:
    search_text = (
        f"inside '{method_name}_test' function" if custom
        else f"inside '{method_name}' function"
    )
    return output.index(search_text, start)


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
    script.parse_args([])
    script.stages_to_run = stages_to_run
    if custom_pre_stage:
        script._run_pre_stage_actions_test = (
            lambda: print("inside '_run_pre_stage_actions_test' function")
        )
    if custom_begin_stage:
        script._begin_stage_test = (
            lambda heading: print("inside '_begin_stage_test' function")
        )
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
    index = 0
    phases = [
        ("_run_pre_stage_actions", custom_pre_stage),
        ("_begin_stage", custom_begin_stage),
        (("run_test", False) if "test" in stages_to_run
         else ("_skip_stage", custom_skip_stage)),
        ("_end_stage", custom_end_stage),
        ("_run_post_stage_actions", custom_post_stage)
    ]
    for method, custom in phases:
        index = ensure_phase_comes_next(
            method,
            captured.out,
            custom=custom,
            start=index
        )


@pytest.mark.parametrize("retry_attempts", [0, 1, 2])
@pytest.mark.parametrize("custom_handle_retry_error", [True, False])
@pytest.mark.parametrize("custom_prepare_to_retry", [True, False])
def test_stage_retry(
    custom_prepare_to_retry: bool,
    custom_handle_retry_error: bool,
    retry_attempts: int,
    capsys: pytest.CaptureFixture
) -> None:
    script = MyAdvancedScript()
    script.parse_args(shlex.split(f"--test-retry-attempts {retry_attempts}"))
    script.stages_to_run = {"test"}
    if custom_prepare_to_retry:
        script._prepare_to_retry_stage_test = (
            lambda retry_state:
                print("inside '_prepare_to_retry_stage_test' function")
        )
    if custom_handle_retry_error:
        script._handle_stage_retry_error_test = (
            lambda retry:
                print("inside '_handle_stage_retry_error_test' function")
        )
    script.run_test(retry=True)
    captured = capsys.readouterr()
    index = 0
    phases = [
        ("_run_pre_stage_actions", False),
        ("_begin_stage", False),
        ("run_test", False),
        ("_end_stage", False)
    ]
    for _ in range(retry_attempts):
        phases += [
            ("_prepare_to_retry_stage", custom_prepare_to_retry),
            ("_begin_stage", False),
            ("run_test", False),
            ("_end_stage", False)
        ]
    phases += [
        ("_handle_stage_retry_error", custom_handle_retry_error),
        ("_run_post_stage_actions", False)
    ]
    for method, custom in phases:
        index = ensure_phase_comes_next(
            method,
            captured.out,
            custom=custom,
            start=index
        )
    if retry_attempts == 0:
        with pytest.raises(ValueError):
            ensure_phase_comes_next(
                "_prepare_to_retry_stage",
                captured.out,
                custom=custom_prepare_to_retry,
                start=0
            )
