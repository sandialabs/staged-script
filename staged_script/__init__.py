"""
The ``staged-script`` package.

Provide the :class:`StagedScript` class, along with some helper classes
and functions.
"""

# © 2024 National Technology & Engineering Solutions of Sandia, LLC
# (NTESS).  Under the terms of Contract DE-NA0003525 with NTESS, the
# U.S. Government retains certain rights in this software.

# SPDX-License-Identifier: BSD-3-Clause

from .staged_script import (
    HelpFormatter,
    RetryStage,
    StageDuration,
    StagedScript,
)

__all__ = [
    "HelpFormatter",
    "RetryStage",
    "StageDuration",
    "StagedScript",
]
__version__ = "2.0.5"
