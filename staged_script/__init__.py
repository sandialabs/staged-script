"""
The ``staged-script`` package.

Provide the :class:`StagedScript` class, along with some helper classes
and functions.
"""

from .staged_script import (
    StagedScript,
    HelpFormatter,
    RetryStage,
    StageDuration,
    lazy_property,
)

__all__ = [
    "StagedScript",
    "HelpFormatter",
    "RetryStage",
    "StageDuration",
    "lazy_property",
]
__version__ = "1.0.0"
