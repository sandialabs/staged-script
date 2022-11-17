#!/usr/bin/env python3
import functools
import re
import shlex
from datetime import datetime, timedelta
from typing import Any, Callable

import rich.traceback
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table

rich.traceback.install()


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
        console (Console):  Used to print rich text to the console.
        current_stage (str):  The name of the stage being run.
        durations (dict[str, timedelta]):  A mapping from stage names to
            how long it took for each to run.
        stage_start_time (datetime):  The time at which a stage began.
        stages_to_run (set[str]):  Which stages to run.
        start_time (datetime):  The time at which this object was
            initialized.
    """

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
        self.console = Console(
            force_terminal=console_force_terminal,
            log_path=console_log_path
        )
        self.current_stage = "CURRENT STAGE NOT SET"
        self.durations: dict[str, timedelta] = {}
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
        self.durations[self.current_stage] = (
            datetime.now() - self.stage_start_time
        )  # yapf: disable
        self.console.log(
            f"`{self.current_stage}` stage duration:  "
            f"{str(self.durations[self.current_stage])}"
        )

    def _skip_stage(self) -> None:
        """
        Execute a series of commands when skipping a stage.
        """
        self.console.log("Skipping this stage.")

    @classmethod
    def stage(
        cls,
        stage_name: str,
        heading: str,
        skip_result: Any = True
    ) -> Callable:
        """
        A decorator to automatically run a series of commands before and
        after every stage.

        Args:
            stage_name:  The name of the stage.
            heading:  A heading message to print indicating what will
                happen in the stage.
            skip_result:  The result to be returned if the stage is
                skipped.
        """

        def decorator(func: Callable) -> Callable:

            @functools.wraps(func)
            def wrapper(self, *args, **kwargs) -> Any:
                self._begin_stage(stage_name, heading)
                try:
                    if stage_name in self.stages_to_run:
                        result = func(self, *args, **kwargs)
                    else:
                        self._skip_stage()
                        result = skip_result
                    self._end_stage()
                    return result
                except Exception as e:
                    self._end_stage()
                    raise e

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
        for stage, duration in self.durations.items():
            table.add_row(stage, str(duration))
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
