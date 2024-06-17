Running Commands
================

Python's :mod:`python:subprocess` module allows interaction with the
underlying shell.  :ref:`StagedScript.run() <running_commands>` is a
lightweight wrapper around :func:`python:subprocess.run`, which includes
the following additional features:

* Allows printing commands in ``--dry-run`` mode.
* Saves the command to a list of commands executed.
* Optionally prints the command before executing it.
* Allows passing additional options to :func:`python:subprocess.run`.
