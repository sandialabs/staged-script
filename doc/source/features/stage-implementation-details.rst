Stage Implementation Details
============================

In order to create a staged script, you need to create your own class
that extends the :ref:`StagedScript <the_stagedscript_class>` base
class.

.. code-block:: python

   from staged_script import StagedScript

   class MyScript(StagedScript):
       ...

You can then define a method as a conceptual stage by using the
:ref:`StagedScript.stage() <the_stage_decorator>` decorator.

.. code-block:: python
   :emphasize-lines: 5-

   from staged_script import StagedScript

   class MyScript(StagedScript):

       @StagedScript.stage("stage-name", "Stage heading")
       def do_the_thing(self) -> None:
           ...

The ``do_the_thing()`` method defines what actually gets run during the
**Stage Body** from :doc:`the-conceptual-stage`.  The decorator handles
automatically running methods for all the other phases of the stage.

Each phase has a :ref:`default implementation <stage_customization>`
provided by the :ref:`StagedScript <the_stagedscript_class>` class.  As
a subclass developer, you can either use the default implementation
as-is, or you can override or extend it in your subclasses.
Additionally, phase implementations can be :ref:`customized on a
stage-by-stage basis <stage_customization>`, in case certain things need
to be done for some, but not all, stages.  Because of this added
flexibility, the complete stage control flow diagram is as follows
(where the nodes in the graph are referring to method names, and
``STAGE_NAME`` would be replaced with the name of the stage you're
customizing):

.. mermaid::
   :zoom:

   %%{init: {"theme": "neutral"}}%%
   flowchart TD
      classDef style_plain fill:#ddd,stroke:#999
      classDef style_pre_stage fill:#fbb,stroke:#b77
      classDef style_begin_stage fill:#ede,stroke:#a9a
      classDef style_end_stage fill:#dfe,stroke:#9ba
      classDef style_post_stage fill:#fdc,stroke:#b98
      classDef style_skip_stage fill:#def,stroke:#9ab
      classDef style_retry_stage fill:#ffc,stroke:#bb8
      linkStyle default color:#000

      entry[stage decorator entry]:::style_plain
      pre_q{{_run_pre_stage_actions_STAGE_NAME exists?}}:::style_pre_stage
      pre_custom(_run_pre_stage_actions_STAGE_NAME):::style_pre_stage
      pre(_run_pre_stage_actions):::style_pre_stage
      begin_q{{_begin_stage_STAGE_NAME exists?}}:::style_begin_stage
      begin_custom(_begin_stage_STAGE_NAME):::style_begin_stage
      begin(_begin_stage):::style_begin_stage
      execute_q{{execute stage?}}:::style_plain
      run(run stage method):::style_plain
      skip_q{{_skip_stage_STAGE_NAME exists?}}:::style_skip_stage
      skip_custom(_skip_stage_STAGE_NAME):::style_skip_stage
      skip(_skip_stage):::style_skip_stage
      end_q{{_end_stage_STAGE_NAME exists?}}:::style_end_stage
      end_custom(_end_stage_STAGE_NAME):::style_end_stage
      end_stage(_end_stage):::style_end_stage
      retry_q{{retry stage?}}:::style_retry_stage
      retry_error_q{{retry error?}}:::style_retry_stage
      retry_error_handler_q{{_handle_stage_retry_error_STAGE_NAME exists?}}:::style_retry_stage
      handle_retry_error_custom(_handle_stage_retry_error_STAGE_NAME):::style_retry_stage
      handle_retry_error(_handle_stage_retry_error):::style_retry_stage
      retry_actions_q{{_prepare_to_retry_stage_STAGE_NAME exists?}}:::style_retry_stage
      retry_actions_custom(_prepare_to_retry_stage_STAGE_NAME):::style_retry_stage
      retry_actions(_prepare_to_retry_stage):::style_retry_stage
      post_q{{_run_post_stage_actions_STAGE_NAME exists?}}:::style_post_stage
      post_custom(_run_post_stage_actions_STAGE_NAME):::style_post_stage
      post(_run_post_stage_actions):::style_post_stage
      exit[stage decorator exit]:::style_plain

      entry --> pre_q
      pre_q -- Yes --> pre_custom
      pre_q -- No --> pre
      pre_custom --> begin_q
      pre --> begin_q
      begin_q -- Yes --> begin_custom
      begin_q -- No --> begin
      begin_custom --> execute_q
      begin --> execute_q
      execute_q -- Yes --> run
      execute_q -- No --> skip_q
      skip_q -- Yes --> skip_custom
      skip_q -- No --> skip
      run --> end_q
      skip_custom --> end_q
      skip --> end_q
      end_q -- Yes --> end_custom
      end_q -- No --> end_stage
      end_custom --> retry_q
      end_stage --> retry_q
      retry_q -- No --> retry_error_q
      retry_error_q -- Yes --> retry_error_handler_q
      retry_error_handler_q -- Yes --> handle_retry_error_custom
      retry_error_handler_q -- No --> handle_retry_error
      handle_retry_error_custom --> post_q
      handle_retry_error --> post_q
      retry_error_q -- No --> post_q
      post_q -- Yes --> post_custom
      post_q -- No --> post
      post_custom --> exit
      post --> exit
      retry_q -- Yes --> retry_actions_q
      retry_actions_q -- Yes --> retry_actions_custom
      retry_actions_q -- No --> retry_actions
      retry_actions_custom --> begin_q
      retry_actions --> begin_q

.. note::

   You can zoom and pan in the image above.
