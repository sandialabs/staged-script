#!/usr/bin/env python3
import functools
import re
import shlex
import subprocess
import sys
from argparse import (
    ArgumentDefaultsHelpFormatter,
    ArgumentParser,
    Namespace,
    RawDescriptionHelpFormatter
)
from datetime import datetime, timedelta
from pathlib import Path
from subprocess import CompletedProcess
from typing import Callable, NamedTuple

import __main__
import rich.traceback
from rich.console import Console, Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from tenacity import RetryCallState, RetryError, Retrying, TryAgain
from tenacity.retry import retry_if_exception_type
from tenacity.stop import stop_after_attempt, stop_after_delay
from tenacity.wait import wait_fixed

sys.path.append(str(Path(__file__).resolve().parents[3] / "python"))
from reverse_argparse import (  # noqa: E402
    ReverseArgumentParser,
    quote_arg_if_necessary
)

rich.traceback.install()


def lazy_property(func: Callable) -> property:
    """
    A decorator to make it such that a property is lazily evaluated.
    When the property is first accessed, the object will not yet have a
    corresponding attribute, so the value will be computed by executing
    :arg:`func`.  Any time the property is accessed thereafter, the
    value will just be retrieved from the object's corresponding
    attribute.

    Args:
        func:  The function used to compute the value of the property.

    Returns:
        The lazy property decorator.
    """
    attr_name = f"_lazy_{func.__name__}"

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return _lazy_property


class StageDuration(NamedTuple):
    stage: str
    duration: timedelta


class HelpFormatter(
    ArgumentDefaultsHelpFormatter,
    RawDescriptionHelpFormatter
):
    """
    Define a formatter class to be used by the argument parser that both
    treats the description as raw text (doesn't do any automatic
    formatting) and shows default values arguments.
    """
    pass


class DriverScript:
    """
    This serves as a base class for any Python scripts intended to drive
    a series of commands in the underlying shell.  It's built around the
    fundamental concept of a "stage", in that such scripts are typically
    broken down into stages, each of which consists of a handful of
    commands.  Certain actions are performed at the beginning or end of
    any given stage, and it's also possible for stages to be skipped.
    The class also provides a means of producing a script execution
    summary to show the user exactly what was done, for the sake of
    replicability and easing debugging.

    Attributes:
        args (Namespace):  The parsed command line arguments for the
            script.
        commands_executed (list[str]):  The commands that were executed
            in the shell.
        console (Console):  Used to print rich text to the console.
        current_stage (str):  The name of the stage being run.
        dry_run (bool):  If ``True``, don't actually run the command
            that would be executed in the shell; instead just print it
            out.
        durations (list[StageDuration]):  A mapping from stage names to
            how long it took for each to run.  This is implemented as a
            ``list`` of named tuples instead of as a ``dict`` to allow
            the flexibility for stages to be run multiple times.
        print_commands (bool):  Whether to print the commands executed
            immediately before executing them.
        retry_arg_group (argparse._ArgumentGroup):  A container within
            the :class:`ArgumentParser` holding all the arguments
            associated with retrying stages.
        script_success (bool):  Subclass developers can toggle this
            attribute to indicate whether the script has succeeded.
        stage_start_time (datetime):  The time at which a stage began.
        stages_to_run (set[str]):  Which stages to run.
        start_time (datetime):  The time at which this object was
            initialized.

    Note that additional attributes are automatically generated for each
    ``stage`` defined by a subclass:
    * ``STAGE_NAME_retry_attempts`` (int):  The number of times to
      attempt retrying the ``STAGE_NAME`` stage.
    * ``STAGE_NAME_retry_attempts_arg`` (argparse.Action):  The
      corresponding argument in the :class:`ArgumentParser`, so subclass
      developers can modify it if needed.
    * ``STAGE_NAME_retry_delay`` (float):  How long to wait (in seconds)
      before attempting to retry the ``STAGE_NAME`` stage.
    * ``STAGE_NAME_retry_delay_arg`` (argparse.Action):  The
      corresponding argument in the :class:`ArgumentParser`, so subclass
      developers can modify it if needed.
    * ``STAGE_NAME_retry_timeout`` (int):  How long to wait (in seconds)
      before giving up on retrying the ``STAGE_NAME`` stage.
    * ``STAGE_NAME_retry_timeout_arg`` (argparse.Action):  The
      corresponding argument in the :class:`ArgumentParser`, so subclass
      developers can modify it if needed.

    Class Variables:
        stages (list[str]):  The stages defined for the script.
    """
    stages: list[str] = []

    def __init__(
        self,
        console_force_terminal: bool | None = None,
        console_log_path: bool = True,
        print_commands: bool = True
    ):
        """
        Initialize a :class:`DriverScript` object.

        Args:
            console_force_terminal:  Whether to force the console to
                behave like a terminal.  ``None`` allows auto-detection.
            console_log_path:  Whether to print the location within a
                file that generated a line in the console log.
            print_commands:  Whether to print the commands executed
                immediately before executing them.

        Note:
            If you override this constructor in a subclass---e.g., to
            create additional attributes, etc.---you'll need to call
            this parent constructor with ``super().__init__()`` and
            optionally pass in any arguments.
        """
        self.args = Namespace()
        self.commands_executed: list[str] = []
        self.console = Console(
            force_terminal=console_force_terminal,
            log_path=console_log_path
        )
        self.current_stage = "CURRENT STAGE NOT SET"
        self.dry_run = False
        self.durations: list[StageDuration] = []
        self.print_commands = print_commands
        self.script_success = True
        self.stage_start_time = datetime.now()
        self.stages_to_run: set[str] = set()
        self.start_time = datetime.now()

    def print_heading(self, message: str, *, color: str = "cyan") -> None:
        """
        Print a heading to indicate at a high level what the script is
        doing.

        Args:
            message:  The message to print.
            color:  What color to print the message in.
        """
        self.console.log(Panel(f"[bold]{message}", style=color))

    def print_dry_run_message(self, message: str, *, indent: int = 0) -> None:
        """
        Print a message indicating that something is happening due to
        the script running in dry-run mode.

        Args:
            message:  The message to print.
            indent:  How many spaces by which to indent that which is
                printed.
        """
        self.console.log(
            Padding(
                Panel(f"DRY-RUN MODE:  {message}", style="yellow"),
                (0, 0, 0, indent)
            )
        )  # yapf: disable

    @staticmethod
    def _add_stage(stage_name: str) -> None:
        """
        Add a new stage to the list of stages.

        Note:
            The `stages` class variable is conceptually an ordered set,
            but Python doesn't have support for such a collection, so
            it's implemented as a value-less `dict` converted to a
            `list`.

        Todo:
            It'd be great to raise a ``ValueError`` if the
            :arg:`stage_name` is already in ``__class__.stages``.  This
            is possible, but it causes problems with ``pytest``, which
            will double-import this module in two different scopes---one
            from the ``__init__.py``, and the other from the test file.
            I haven't yet figured out a workaround other than to tell
            the user to ensure they use unique stage names.

        Args:
            stage_name:  The name of the stage, which must consist of
                only lowercase letters, both to simplify implementation
                details elsewhere in the class, and to provide the best
                user experience for users of your :class:`DriverScript`
                subclasses.

        Raises:
            RuntimeError:  If the stage name is invalid.
        """
        if not re.match("^[a-z]+$", stage_name):
            raise ValueError(
                f"Stage name '{stage_name}' must contain only lowercase "
                "letters."
            )
        if stage_name in __class__.stages:
            print(
                "Warning:  It looks like you're redefining the "
                f"'{stage_name}' stage.  Stage names within a 'DriverScript' "
                "subclass must be unique."
            )
        __class__.stages = list(dict.fromkeys(__class__.stages + [stage_name]))

    def _run_pre_stage_actions(self) -> None:
        """
        Run a series of commands before a stage actually starts.  This
        is implemented here as a no-op, but subclass developers can
        override it if they wish to always perform certain actions
        before stages get underway (e.g., maybe you want to log some
        details on the state of the system, etc.).

        Subclass developers can also customize the **Pre-Stage Actions**
        for an individual stage by defining a
        ``_run_pre_stage_actions_STAGE_NAME`` method, where
        ``STAGE_NAME`` should be replaced with the name of the stage
        (the first argument to the :func:`stage` decorator).  This can
        be useful if, e.g., you wanted to ensure certain pre-conditions
        were met before attempting the stage, and erroring out
        appropriately if not.
        """
        pass

    def _begin_stage(self, heading: str) -> None:
        """
        Execute a series of commands at the beginning of every stage.

        If subclass developers wish to extend the **Begin-Stage
        Actions**, they can do so with the following:

        .. code-block:: python

            def _begin_stage(
                self,
                heading: str
            ) -> None:
                super()._begin_stage(heading)
                # Insert more actions here.

        Alternatively you can override the default behavior entirely by
        omitting the `super()` line above.

        In addition, you may wish to customize the **Begin-Stage
        Actions** for a particular stage, in which case you define a
        ``_begin_stage_STAGE_NAME`` method, where ``STAGE_NAME`` should
        be replaced with the name of the stage (the first argument to
        the :func:`stage` decorator), e.g.:

        .. code-block:: python

            def _begin_stage_test(  # Particular to the 'test' stage.
                self,
                heading: str
            ) -> None:
                self._begin_stage(heading)  # Optional
                # Insert more actions here.

        Args:
            heading:  A heading message to print indicating what will
                happen in the stage.
        """
        self.stage_start_time = datetime.now()
        self.print_heading(heading)

    def _skip_stage(self) -> None:
        """
        Execute a series of commands when skipping a stage.

        If subclass developers wish to extend the **Skip-Stage
        Actions**, they can do so with the following:

        .. code-block:: python

            def _skip_stage(self) -> None:
                super()._skip_stage()
                # Insert more actions here.

        Alternatively you can override the default behavior entirely by
        omitting the `super()` line above.

        In addition, you may wish to customize the **Skip-Stage
        Actions** for a particular stage, in which case you define a
        ``_skip_stage_STAGE_NAME`` method, where ``STAGE_NAME`` should
        be replaced with the name of the stage (the first argument to
        the :func:`stage` decorator), e.g.:

        .. code-block:: python

            # Particular to the 'test' stage.
            def _skip_stage_test(self) -> None:
                self._skip_stage()  # Optional
                # Insert more actions here.
        """
        self.console.log("Skipping this stage.")

    def _end_stage(self) -> None:
        """
        Execute a series of commands at the end of every stage.

        If subclass developers wish to extend the **End-Stage Actions**,
        they can do so with the following:

        .. code-block:: python

            def _end_stage(self) -> None:
                super()._end_stage()
                # Insert more actions here.

        Alternatively you can override the default behavior entirely by
        omitting the `super()` line above.

        In addition, you may wish to customize the **End-Stage Actions**
        for a particular stage, in which case you define an
        ``_end_stage_STAGE_NAME`` method, where ``STAGE_NAME`` should
        be replaced with the name of the stage (the first argument to
        the :func:`stage` decorator), e.g.:

        .. code-block:: python

            # Particular to the 'test' stage.
            def _end_stage_test(self) -> None:
                self._end_stage()  # Optional
                # Insert more actions here.
        """
        stage_duration = datetime.now() - self.stage_start_time
        self.durations.append(
            StageDuration(self.current_stage, stage_duration)
        )  # yapf: disable
        self.console.log(
            f"`{self.current_stage}` stage duration:  {str(stage_duration)}"
        )

    def _run_post_stage_actions(self) -> None:
        """
        Run a series of commands after a stage wraps up.  This is
        implemented here as a no-op, but subclass developers can
        override it if they wish to always perform certain actions
        after stages complete and before execution moves on with the
        rest of the script (e.g., maybe you want to log some details on
        the state of the system, etc.).

        Subclass developers can also customize the **Post-Stage
        Actions** for an individual stage by defining a
        ``_run_post_stage_actions_STAGE_NAME`` method, where
        ``STAGE_NAME`` should be replaced with the name of the stage
        (the first argument to the :func:`stage` decorator).  This can
        be useful if, e.g., you wanted to ensure certain post-conditions
        were met before moving on, and erroring out appropriately if
        not.
        """
        pass

    def _prepare_to_retry_stage(self, retry_state: RetryCallState) -> None:
        """
        Prepare to retry a stage.  This method will be executed after
        the **End-Stage Actions** of one attempt and before the
        **Begin-Stage Actions** of a following attempt.

        If subclass developers wish to extend the **Prepare-to-Retry
        Actions**, they can do so with the following:

        .. code-block:: python

            def _prepare_to_retry_stage(
                self,
                retry_state: RetryCallState
            ) -> None:
                super()._prepare_to_retry_stage(retry_state)
                # Insert more actions here.

        Alternatively you can override the default behavior entirely by
        omitting the `super()` line above.

        In addition, you may wish to customize the **Prepare-to-Retry
        Actions** for an individual stage by defining a
        ``_prepare_to_retry_stage_STAGE_NAME`` method, where
        ``STAGE_NAME`` should be replaced with the name of the stage
        (the first argument to the :func:`stage` decorator), e.g.:

        .. code-block:: python

            # Particular to the 'test' stage.
            def _prepare_to_retry_stage_test(
                self,
                retry_state: RetryCallState
            ) -> None:
                self._prepare_to_retry_stage(retry_state)  # Optional
                # Insert more actions here.

        This can be useful if, e.g., you need to reset some state before
        running a particular stage again.

        Args:
            retry_state:  Information regarding the retry operation in
                progress.
        """
        self.console.log(
            f"[bold yellow]Preparing to retry the '{self.current_stage}' "
            f"stage...[/]\n{retry_state}"
        )

    def _handle_stage_retry_error(
        self,
        retry: Retrying
    ) -> None:
        """
        When a stage has exhausted the specified retry conditions,
        handle the thrown :class:`RetryError` appropriately.

        If subclass developers wish to extend the **Retry Error
        Handler**, they can do so with the following:

        .. code-block:: python

            def _handle_stage_retry_error(
                self,
                retry: Retrying
            ) -> None:
                super()._handle_stage_retry_error(retry)
                # Insert more actions here.

        Alternatively you can override the default behavior entirely by
        omitting the `super()` line above.

        In addition, you may wish to customize the **Retry Error
        Handler** for an individual stage by defining a
        ``_handle_stage_retry_error_STAGE_NAME`` method, where
        ``STAGE_NAME`` should be replaced with the name of the stage
        (the first argument to the :func:`stage` decorator), e.g.:

        .. code-block:: python

            # Particular to the 'test' stage.
            def _handle_stage_retry_error_test(
                self,
                retry: Retrying
            ) -> None:
                self._handle_stage_retry_error(retry)  # Optional
                # Insert more actions here.

        Args:
            retry:  The :class:`Retrying` controller, which contains
                information about the retrying that was done.
        """
        retry_attempts = getattr(
            self,
            f"{self.current_stage}_retry_attempts",
            0
        )
        if retry_attempts > 0:
            stage_time = timedelta(
                seconds=retry.statistics["delay_since_first_attempt"]
            )
            self.console.log(self.print_heading(
                f"Abandoning retrying the '{self.current_stage}' stage.  "
                f"Total attempts:  {retry.statistics['attempt_number']}.  "
                f"Total time:  {stage_time}.",
                color="red"
            ))

    @staticmethod
    def stage(
        stage_name: str,
        heading: str
    ) -> Callable:
        """
        A decorator to take a function and convert it to a conceptual
        stage of a script.  Each stage consists of the following phases:

        Pre-Stage Actions
            A series of commands to run before a stage technically
            begins.  See :func:`_run_pre_stage_actions`.
        Begin-Stage Actions
            A series of commands to run at the beginning of the stage.
            See :func:`_begin_stage`.
        Stage Body
            The actual work of the stage itself, encapsulated in the
            decorated function.  However, if a particular stage is not
            to be executed (if it's not passed in with the ``--stage``
            flag on the command line), then there's also the concept of
            **Skip-Stage Actions**, which are a series of commands to
            run if a stage is to be skipped.  See :func:`_skip_stage`.
        End-Stage Actions
            A series of commands to run at the end of the stage, even if
            an exception was raised within the **Stage Body**.  See
            :func:`_end_stage`.
        Post-Stage Actions
            A series of commands to run after a stage has technically
            wrapped up.  See :func:`_run_post_stage_actions`.

        If a subclass developer writes a function to be wrapped by this
        decorator such that it raises a :class:`tenacity.TryAgain`
        exception on certain failure conditions, then there are
        additional **Prepare-to-Retry Actions**, which are a series of
        commands to run before the next attempt at running the stage
        (see :func:`_prepare_to_retry_stage`).  The **Begin-Stage
        Actions**, **Stage Body**, and **End-Stage Actions** are wrapped
        in this retry loop, while the **Pre-** and **Post-Stage
        Actions** are not.

        If the retry specifications (see :func:`parser`) are exhausted
        and the wrapped function still raises a :class:`TryAgain`, then
        there is a **Retry Error Handler** containing a series of
        commands to run when exiting the retry loop (see
        :func:`_handle_stage_retry_error`).

        Args:
            stage_name:  The name of the stage, which must consist of
                only lowercase letters.  Note that stage names must be
                unique within a class that inherits from
                :class:`DriverScript`.
            heading:  A heading message to print indicating what will
                happen in the stage.
        """
        __class__._add_stage(stage_name)

        def decorator(func: Callable) -> Callable:

            def get_phase_method(self, method_name: str) -> Callable:
                """
                Get the method to run for a phase of a stage.

                Args:
                    method_name:  The name of the default method for the
                        phase (e.g., ``"_begin_stage"``).

                Returns:
                    Either a stage-specific method (e.g.,
                    ``_begin_stage_STAGE_NAME``), if one exists, or the
                    default implementation (e.g., :func:`_begin_stage`)
                    otherwise.
                """
                custom_method = getattr(
                    self,
                    f"{method_name}_{stage_name}",
                    False
                )
                return custom_method or getattr(self, method_name)

            def run_retryable_phases(self, *args, **kwargs) -> None:
                """
                Run the phases of the stage that are "retryable," namely
                the begin-stage actions, stage body (including skip
                actions, if applicable), and end-stage actions.  When a
                stage is automatically retried, these phases will be run
                again.

                Args:
                    args: The positional arguments to pass on to the
                        phase method.
                    kwargs: The keyword arguments to pass on to the
                        phase method.

                Raises:
                    Exception:  If an exception is thrown in the stage
                        body function, it will be caught such that the
                        end-stage actions can be run, but then it will
                        be re-raised so it can propagate upward.
                """
                get_phase_method(self, "_begin_stage")(heading)
                if self.current_stage not in self.stages_to_run:
                    get_phase_method(self, "_skip_stage")()
                else:
                    try:
                        func(self, *args, **kwargs)
                    except Exception as e:
                        get_phase_method(self, "_end_stage")()
                        raise e
                get_phase_method(self, "_end_stage")()

            @functools.wraps(func)
            def wrapper(self, *args, **kwargs) -> None:
                """
                Wrap the given ``func`` in the various phases of a
                conceptual stage.
                """
                self.current_stage = stage_name
                get_phase_method(self, "_run_pre_stage_actions")()
                timeout = getattr(self, f"{stage_name}_retry_timeout")
                attempts = getattr(self, f"{stage_name}_retry_attempts")
                delay = getattr(self, f"{stage_name}_retry_delay")
                stop_after_timeout = stop_after_delay(timeout)
                stop_after_max_attempts = stop_after_attempt(attempts + 1)
                retry = Retrying(
                    retry=retry_if_exception_type(TryAgain),
                    stop=(stop_after_timeout | stop_after_max_attempts),
                    wait=wait_fixed(delay),
                    before_sleep=get_phase_method(
                        self,
                        "_prepare_to_retry_stage"
                    )
                )
                try:
                    retry(run_retryable_phases, self, *args, **kwargs)
                except RetryError:
                    get_phase_method(self, "_handle_stage_retry_error")(retry)
                get_phase_method(self, "_run_post_stage_actions")()

            return wrapper

        return decorator

    def get_timing_report(self) -> Table:
        """
        Create a report of the durations of all the stages.

        Returns:
            The report, formatted as a table.
        """
        table = Table(show_footer=True)
        table.add_column(header="Stage", footer="Total")
        table.add_column(
            header="Duration",
            footer=str(datetime.now() - self.start_time)
        )
        for _ in self.durations:
            table.add_row(_.stage, str(_.duration))
        return table

    @staticmethod
    def _current_arg_is_long_flag(args: list[str]) -> bool:
        """
        Determine if the first argument in the list is a long flag.

        Args:
            args:  The list of arguments to a command.

        Returns:
            ``True`` if the first argument starts with ``--``.
        """
        return len(args) > 0 and args[0].startswith("--")

    @staticmethod
    def _next_arg_is_flag(args: list[str]) -> bool:
        """
        Determine if the second argument in the list is a flag.

        Args:
            args:  The list of arguments to a command.

        Returns:
            ``True`` if the second argument starts with ``-``.
        """
        return len(args) > 1 and args[1].startswith("-")

    def pretty_print_command(self, command: str, indent: int = 4) -> str:
        """
        Take a command executed in the shell and pretty-print it by
        inserting newlines where appropriate:

        * A long-style flag with an argument is placed on its own line,
          e.g., ``--foo bar``.
        * A long-style flag without an argument is placed on its own
          line.
        * Any other arguments (e.g., short-style flags, positional
          arguments) are placed on their own lines.

        Args:
            command:  The input command.
            indent:  How many spaces to indent each subsequent line.

        Returns:
            The reformatted command.
        """
        args = shlex.split(command)
        lines = [args.pop(0)]
        while args:
            if (not self._current_arg_is_long_flag(args)
                    or self._next_arg_is_flag(args)
                    or len(args) == 1):  # yapf: disable
                lines.append(args.pop(0))
            else:
                lines.append(
                    f"{args.pop(0)} {quote_arg_if_necessary(args.pop(0))}"
                )
        return (" \\\n" + " "*indent).join(lines)

    @lazy_property
    def parser(self) -> ArgumentParser:
        """
        Create an :class:`ArgumentParser` for all the arguments made
        available by this base class.  This should be overridden in
        subclasses as follows:

        .. code-block:: python

            @lazy_property
            def parser(self) -> ArgumentParser:
                ap = super().parser
                ap.description = '''INSERT DESCRIPTION HERE'''
                ap.add_argument("--foo", ...)
                ...
                # Optional changes.
                ap.formatter_class = RawDescriptionHelpFormatter
                ap.set_defaults(stage=self.stages)
                return ap

        The formatter class defaults to a combination of
        :class:`ArgumentDefaultsHelpFormatter` and
        :class:`RawDescriptionHelpFormatter`, but can optionally be set
        to whatever you like.

        If you'd like to set the default value for the ``--stage``
        argument, you can use :func:`set_defaults` (the example above
        defaults to all the stages in the order in which they were
        defined).

        Similarly, if you wish to override the default values for the
        retry arguments that are automatically provided for every stage,
        you can do so with, e.g.:

        .. code-block:: python

            ap.set_defaults(
                foo_retry_attempts=5,
                foo_retry_delay=10,
                foo_retry_timeout=600
            )

        If you wish to suppress the stage retry arguments for your
        stages that don't raise a :class:`tenacity.TryAgain` exception,
        you can do so with, e.g.:

        .. code-block:: python

            self.foo_retry_attempts_arg.help = argparse.SUPPRESS
            self.foo_retry_delay_arg.help = argparse.SUPPRESS
            self.foo_retry_timeout_arg.help = argparse.SUPPRESS

        And if you want to remove the title for the retry group
        altogether, you can do so with:

        .. code-block:: python

            self.retry_arg_group.title = argparse.SUPPRESS

        Returns:
            The base argument parser.
        """
        description = (
            "This is the description of the ArgumentParser in the "
            "DriverScript base class.  This should be overridden in your "
            "subclass.  See the docstring for details."
        )
        ap = ArgumentParser(
            description=description,
            formatter_class=HelpFormatter
        )
        ap.add_argument(
            "--stage",
            choices=self.stages,
            nargs="+",
            help="Which stages to run."
        )
        ap.add_argument(
            "--dry-run",
            action="store_true",
            help="If specified, don't actually run the commands in the shell; "
            "instead print the commands that would have been executed."
        )
        if self.stages:
            self.retry_arg_group = ap.add_argument_group(
                "retry",
                "Additional options for retrying stages."
            )
            for stage in self.stages:
                retry_attempts = self.retry_arg_group.add_argument(
                    f"--{stage}-retry-attempts",
                    default=0,
                    type=int,
                    help=f"How many times to retry the '{stage}' stage."
                )
                setattr(self, f"{stage}_retry_attempts_arg", retry_attempts)
                retry_delay = self.retry_arg_group.add_argument(
                    f"--{stage}-retry-delay",
                    default=0,
                    type=float,
                    help="How long to wait (in seconds) before retrying the "
                    f"'{stage}' stage."
                )
                setattr(self, f"{stage}_retry_delay_arg", retry_delay)
                retry_timeout = self.retry_arg_group.add_argument(
                    f"--{stage}-retry-timeout",
                    default=60,
                    type=int,
                    help="How long to wait (in seconds) before giving up on "
                    f"retrying the '{stage}' stage."
                )
                setattr(self, f"{stage}_retry_timeout_arg", retry_timeout)
        return ap

    def parse_args(self, argv: list[str]) -> None:
        """
        Parse the command line arguments supplied by this base class.
        This should be overridden in subclasses as follows:

        .. code-block:: python

            def parse_args(self, argv: list[str]) -> None:
                super().parse_args(argv)
                # Parse additional arguments and store as attributes.
                self.foo = self.args.foo
                ...
                # Ensure supplied arguments are valid, etc.
                ...

        Args:
            argv:  The command line arguments used when running this
                file as a script.
        """
        self.args = self.parser.parse_args(argv)
        self.dry_run = self.args.dry_run
        self.stages_to_run = (
            set(self.args.stage) if self.args.stage is not None else set()
        )
        for stage in self.stages:
            for retry_arg in [
                f"{stage}_retry_attempts",
                f"{stage}_retry_delay",
                f"{stage}_retry_timeout"
            ]:
                setattr(self, retry_arg, getattr(self.args, retry_arg, None))

    def run(
        self,
        command: str,
        pretty_print: bool = False,
        print_command: bool | None = None,
        **kwargs
    ) -> CompletedProcess:
        """
        Run a command in the underlying shell.

        Args:
            command:  The command to be executed.
            pretty_print:  Whether the command should be
                "pretty-printed" when storing it in the list of commands
                executed.
            print_command:  Whether to print the command executed
                immediately before executing it.  If specified, this
                overrides the :attr:`print_commands` specified when
                instantiating the class.
            kwargs:  Additional keyword arguments to pass on to
                :func:`subprocess.run`.

        Returns:
            The result from calling :func:`subprocess.run()`.
        """
        if self.dry_run:
            self.print_dry_run_message(
                f"The command executed would be:  `{command}`"
            )
            return CompletedProcess(
                args=f"echo {command}",
                returncode=0,
                stdout=command
            )
        self.commands_executed.append(
            self.pretty_print_command(command) if pretty_print else command
        )
        if (
            print_command is True
            or (print_command is None and self.print_commands is True)
        ):
            self.console.log(f"Executing:  {command}")
        return subprocess.run(command, **kwargs)

    def raise_parser_error(self, message):
        """
        Exit the script with a message indicating what went wrong when
        parsing the command line arguments.

        Args:
            message:  What went wrong.

        Raises:
            SystemExit:  To indicate the problem and stop script
                execution.
        """
        self.parser.print_help()
        self.console.print(f"[yellow]\n{message}")
        raise SystemExit(1)

    def print_script_execution_summary(
        self,
        extra_sections: dict[str, str] | None = None
    ) -> None:  # yapf: disable
        """
        Print a summary of everything that was done by the script.

        Args:
            extra_sections:  Any sections to add to the summary in
                addition to what's automatically supplied by this base
                class.  The keys are section headings, and values are
                the associated details.  If you provide section headings
                identical to any supplied by this base class, the
                corresponding details will override that which is
                provided by default.

        Note:  If you wish to override this in a subclass for the sake
        of providing additional sections every time it's called, you can
        do something like the following:

        .. code-block:: python

            def print_script_execution_summary(
                self,
                extra_sections: dict[str, str] | None = None
            ) -> None:
                extras = {"Additional section": "With some details."}
                if extra_sections is not None:
                    extras.update(extra_sections)
                super().print_script_execution_summary(
                    extra_sections=extras
                )
        """
        unparser = ReverseArgumentParser(self.parser, self.args)
        sections = {
            "Ran the following": unparser.get_pretty_command_line_invocation(),
            "Commands executed": "\n".join(self.commands_executed),
            "Timing results": self.get_timing_report(),
            "Script result": (
                "[bold green]Success" if self.script_success
                else "[bold red]Failure"
            )
        }
        if extra_sections is not None:
            sections |= extra_sections
        items = [""]
        for section, details in sections.items():
            items.extend([f"➤ {section}:", Padding(details, (1, 0, 1, 4))])
        title = f"{Path(__main__.__file__).name} Script Execution Summary"
        self.console.rule(title)
        self.console.log(Group(*items))
        self.console.rule(f"End {title}")
