Script Execution Summary
========================

In order to improve replicability and ease debugging, ``StagedScript``
also allows you to :ref:`print a summary of everything that was done
<script_execution_summary>` when the script exits.  By default, this
summary includes the following details:

* What the user ran from the command line, including any default values.
  (This functionality is provided by the `reverse-argparse`_ package.)
* What commands were executed under the hood.
* A report of how long each stage took.
* Whether the script passed or failed.

.. _reverse-argparse:  https://github.com/sandialabs/reverse_argparse/

As with all things in ``StagedScript``, this, too, is intended to be
extended by subclasses.
