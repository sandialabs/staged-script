#!/usr/bin/env python3
import functools
import re
import shlex
import subprocess
import sys
from argparse import ArgumentParser, Namespace
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable, NamedTuple

import __main__
import rich.traceback
from rich.console import Console, Group
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table

sys.path.append(str(Path(__file__).resolve().parents[3] / "python"))
from reverse_argparse import ReverseArgumentParser  # noqa: E402

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
        stage_start_time (datetime):  The time at which a stage began.
        stages_to_run (set[str]):  Which stages to run.
        start_time (datetime):  The time at which this object was
            initialized.

    Class Variables:
        stages (list[str]):  The stages defined for the script.
    """
    stages: list[str] = []

    def __init__(
        self,
        console_force_terminal: bool | None = None,
        console_log_path: bool = True
    ):
        """
        Initialize a :class:`DriverScript` object.

        Args:
            console_force_terminal:  Whether to force the console to
                behave like a terminal.  ``None`` allows auto-detection.
            console_log_path:  Whether to print the location within a
                file that generated a line in the console log.

        Note:
            If you override this constructor in a child class---e.g., to
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
        TODO:  INSERT DOCSTRING.
        """
        pass

    def _begin_stage(self, stage_name: str, heading: str) -> None:
        """
        Execute a series of commands at the beginning of every stage.

        Args:
            stage_name:  The name of the stage.
            heading:  A heading message to print indicating what will
                happen in the stage.
        """
        self.stage_start_time = datetime.now()
        self.current_stage = stage_name
        self.print_heading(heading)

    def _end_stage(self) -> None:
        """
        Execute a series of commands at the end of every stage.
        """
        stage_duration = datetime.now() - self.stage_start_time
        self.durations.append(
            StageDuration(self.current_stage, stage_duration)
        )  # yapf: disable
        self.console.log(
            f"`{self.current_stage}` stage duration:  {str(stage_duration)}"
        )

    def _skip_stage(self) -> None:
        """
        Execute a series of commands when skipping a stage.
        """
        self.console.log("Skipping this stage.")

    @staticmethod
    def stage(
        stage_name: str,
        heading: str,
        skip_result: Any = True
    ) -> Callable:
        """
        A decorator to automatically run a series of commands before and
        after every stage.

        TODO:  UPDATE DOCSTRING.

        Args:
            stage_name:  The name of the stage.  Note that stage names
                must be unique within a class that inherits from
                :class:`DriverScript`.
            heading:  A heading message to print indicating what will
                happen in the stage.
            skip_result:  The result to be returned if the stage is
                skipped.
        """
        __class__._add_stage(stage_name)

        def decorator(func: Callable) -> Callable:

            def run_pre_stage_phase(self) -> None:
                run_custom_pre_stage_actions = getattr(
                    self,
                    f"_run_pre_{stage_name}_stage_actions",
                    False
                )
                if run_custom_pre_stage_actions:
                    run_custom_pre_stage_actions()
                else:
                    self._run_pre_stage_actions()

            @functools.wraps(func)
            def wrapper(self, *args, **kwargs) -> Any:
                run_pre_stage_phase(self)
                try:
                    self._begin_stage(stage_name, heading)
                    if stage_name in self.stages_to_run:
                        result = func(self, *args, **kwargs)
                    else:
                        self._skip_stage()
                        result = skip_result
                    return result
                finally:
                    self._end_stage()

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

    @staticmethod
    def _quote_arg(arg: str) -> str:
        """
        If an argument to a command has any spaces in it, surround it in
        single quotes.  If no quotes are necessary, don't change the
        argument.

        Args:
            arg:  The command line argument.

        Returns:
            The (possibly) quoted argument.
        """
        spaces_in_string = re.compile(r"(.*\s.*)")
        return (
            spaces_in_string.sub(r"'\1'", arg)
            if spaces_in_string.search(arg) else arg
        )  # yapf: disable

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
                lines.append(f"{args.pop(0)} {self._quote_arg(args.pop(0))}")
        return (" \\\n" + " "*indent).join(lines)

    @lazy_property
    def parser(self) -> ArgumentParser:
        """
        Create an :class:`ArgumentParser` for all the arguments made
        available by this base class.  This should be overridden in
        child classes as follows:

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

        The formatter class can optionally be set to something other
        than the default, and if you'd like to set the default value for
        the ``--stage`` argument, you can use :func:`set_defaults` (the
        example above defaults to running all the stages in the order in
        which they were defined).

        Returns:
            The base argument parser.
        """
        description = """
This is the description of the ArgumentParser in the DriverScript base
class.  This should be overridden in your child class.  See the
docstring for details.
"""
        ap = ArgumentParser(description=description)
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
        return ap

    def parse_args(self, argv: list[str]) -> None:
        """
        Parse the command line arguments supplied by this base class.
        This should be overridden in child classes as follows:

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
        self.stages_to_run = set(self.args.stage)

    def run(
        self,
        command: str,
        pretty_print: bool = False,
        **kwargs
    ) -> subprocess.CompletedProcess:
        """
        Run a command in the underlying shell.

        Args:
            command:  The command to be executed.
            pretty_print:  Whether the command should be
                "pretty-printed" when storing it in the list of commands
                executed.
            kwargs:  Additional keyword arguments to pass on to
                :func:`subprocess.run`.

        Returns:
            The result from calling :func:`subprocess.run()`.
        """
        self.commands_executed.append(
            self.pretty_print_command(command) if pretty_print else command
        )
        self.console.log(f"Executing:  {command}")
        return subprocess.run(command, **kwargs)

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

        Note:  If you wish to override this in a child class for the
        sake of providing additional sections every time it's called,
        you can do something like the following:

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
            "Timing results": self.get_timing_report()
        }
        if extra_sections is not None:
            sections.update(extra_sections)
        items = [""]
        for section, details in sections.items():
            items.extend([f"➤ {section}:", Padding(details, (1, 0, 1, 4))])
        title = f"{Path(__main__.__file__).name} Script Execution Summary"
        self.console.rule(title)
        self.console.log(Group(*items))
        self.console.rule(f"End {title}")
