"""Integration tests for an advanced ``staged-script`` use case."""
import shlex

import pytest
from rich.console import Console
from tenacity import RetryCallState, Retrying, TryAgain

from python.staged_script.staged_script.staged_script import StagedScript


class MyAdvancedScript(StagedScript):
    """
    An advanced staged script.

    A stage method is defined, and the various phase methods are
    overridden.
    """

    @StagedScript.stage("test", "Test stage")
    def run_test(self, retry: bool = False) -> None:
        """
        A stage that might need to be retried.

        Args:
            retry:  Whether the stage should be retried.

        Raises:
            TryAgain:  If the stage needs to be retried.
        """
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


@pytest.fixture()
def mas() -> MyAdvancedScript:
    """Create a :class:`MyAdvancedScript` object to be used by tests."""
    my_advanced_script = MyAdvancedScript({"test"})
    my_advanced_script.console = Console(log_time=False, log_path=False)
    return my_advanced_script


def ensure_phase_comes_next(
    method_name: str,
    output: str,
    custom: bool = False,
    start: int = 0
) -> int:
    """
    A helper to check the sequencing of the output.

    Find where the output text corresponding to a particular phase
    occurs in the ``stdout`` of the test.

    Args:
        method_name:  The name of the method for the phase.
        output:  The output text to search.
        custom:  Whether to use the custom phase method vs the default
            implementation.
        start:  Where to start searching in the output string.

    Returns:
        The index of the phase output text in the output string.
    """
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
    mas: MyAdvancedScript,
    capsys: pytest.CaptureFixture
) -> None:
    """
    Ensure the various phases of the stage run in the appropriate order.

    This case does not include retrying the stage.
    """
    mas.parse_args([])
    mas.stages_to_run = stages_to_run
    if custom_pre_stage:
        mas._run_pre_stage_actions_test = (
            lambda: print("inside '_run_pre_stage_actions_test' function")
        )
    if custom_begin_stage:
        mas._begin_stage_test = (
            lambda heading: print("inside '_begin_stage_test' function")
        )
    if custom_skip_stage:
        mas._skip_stage_test = (
            lambda: print("inside '_skip_stage_test' function")
        )
    if custom_end_stage:
        mas._end_stage_test = (
            lambda: print("inside '_end_stage_test' function")
        )
    if custom_post_stage:
        mas._run_post_stage_actions_test = (
            lambda: print("inside '_run_post_stage_actions_test' function")
        )
    mas.run_test()
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
    mas: MyAdvancedScript,
    capsys: pytest.CaptureFixture
) -> None:
    """
    Ensure the various phases of the stage run in the appropriate order.

    This case includes retrying the stage.
    """
    mas.parse_args(shlex.split(f"--test-retry-attempts {retry_attempts}"))
    mas.stages_to_run = {"test"}
    if custom_prepare_to_retry:
        mas._prepare_to_retry_stage_test = (
            lambda retry_state:
                print("inside '_prepare_to_retry_stage_test' function")
        )
    if custom_handle_retry_error:
        mas._handle_stage_retry_error_test = (
            lambda retry:
                print("inside '_handle_stage_retry_error_test' function")
        )
    mas.run_test(retry=True)
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
