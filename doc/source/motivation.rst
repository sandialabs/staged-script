Motivation
==========

Python is an ideal language for certain types of software infrastructure
automation for a variety of reasons:

* It has a community-accepted style guide (`PEP 8`_), adherence to
  which makes it easy for software engineers to transition between
  projects and come up to speed quickly and easily.
* It has a powerful and feature-rich testing framework (`pytest`_),
  enabling comprehensive automating testing of a code base.
* There are documentation guidelines and tools (`PEP 257`_, `Google
  docstring format`_, `Sphinx`_), along with an established community
  history of thorough package documentation.
* Various linters exist (`Ruff`_) to automate and enforce adherence to
  much of the above.
* The language is object oriented, enabling the development of
  ecosystems of modular, reusable components.

.. _PEP 8:  https://peps.python.org/pep-0008/
.. _pytest:  https://docs.pytest.org/
.. _PEP 257:  https://peps.python.org/pep-0257/
.. _Google docstring format:  https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _Sphinx:  https://www.sphinx-doc.org/
.. _Ruff:  https://docs.astral.sh/ruff/

Automating what a user does manually often involves walking through a
series of *stages*.  E.g., first we need to do this one thing, then we
need to do this other thing, and finally wrap up with this third thing.
Each conceptual stage has the same general form, where you may wish
to execute certain actions at the beginning or end of each stage, to
check certain pre- or post-conditions before/after execution, etc.  See
:doc:`features/the-conceptual-stage` for more details.

In such scripts, you often need to execute commands in the underlying
shell.  Bash alone is less than ideal for such robust scripting, because
it lacks many of Python's features listed above.\ [#bash]_  When you
need to use Python to interact with the underlying shell, the
:mod:`python:subprocess` library exists; however, it's laser-focused on just
providing shell interaction, and users often wind up writing little
wrappers around it to add functionality or convenience for their
particular use cases.

The questions then are:

* Can we create a tool to help ease the development of such automation
  scripts?
* Can it be easy to get started with, but also provide substantial
  power-user functionality?

``staged-script`` is just such a tool.

.. rubric:: Footnotes

.. [#bash]

   For the sticklers out there, yes, I realize it is possible to unit
   test bash scripts, and it's *technically* possible to hack bash into
   behaving as if it supports object-oriented programming.  In both
   instances, the user experience is a far cry from what is afforded by
   a full-featured programming language like Python.  Bash was never
   intended to be that---it's a shell language, first and foremost.
