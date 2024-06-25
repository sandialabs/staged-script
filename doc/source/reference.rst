Reference
=========

.. automodule:: staged_script.staged_script
   :no-members:

.. _the_stagedscript_class:

The StagedScript Class
----------------------

.. autoclass:: staged_script.staged_script.StagedScript
   :no-members:

.. _the_stage_decorator:

Stage Definition
^^^^^^^^^^^^^^^^

.. autodecorator:: staged_script.staged_script.StagedScript.stage

.. _stage_customization:

Stage Customization
^^^^^^^^^^^^^^^^^^^

.. automethod:: staged_script.staged_script.StagedScript._run_pre_stage_actions
.. automethod:: staged_script.staged_script.StagedScript._begin_stage
.. automethod:: staged_script.staged_script.StagedScript._skip_stage
.. automethod:: staged_script.staged_script.StagedScript._end_stage
.. automethod:: staged_script.staged_script.StagedScript._run_post_stage_actions

.. _customizing_retry_behavior:

.. automethod:: staged_script.staged_script.StagedScript._prepare_to_retry_stage
.. automethod:: staged_script.staged_script.StagedScript._handle_stage_retry_error

.. _parsing_arguments:

Parsing Arguments
^^^^^^^^^^^^^^^^^

.. autoproperty:: staged_script.staged_script.StagedScript.parser

.. _parse_args:

.. automethod:: staged_script.staged_script.StagedScript.parse_args
.. automethod:: staged_script.staged_script.StagedScript.raise_parser_error

.. _running_commands:

Running Commands
^^^^^^^^^^^^^^^^

.. automethod:: staged_script.staged_script.StagedScript.run
.. automethod:: staged_script.staged_script.StagedScript.pretty_print_command

.. _script_execution_summary:

Script Execution Summary
^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: staged_script.staged_script.StagedScript.print_script_execution_summary

Additional Methods
^^^^^^^^^^^^^^^^^^

.. automethod:: staged_script.staged_script.StagedScript.print_heading
.. automethod:: staged_script.staged_script.StagedScript.print_dry_run_message

Helper Classes
--------------

.. autoclass:: staged_script.staged_script.StageDuration

.. _retry_stage_exception:

.. autoclass:: staged_script.staged_script.RetryStage
.. autoclass:: staged_script.staged_script.HelpFormatter
