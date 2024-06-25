The Conceptual Stage
====================

The Basics
----------

.. sidebar::

   .. mermaid::
      :align: center
      :caption: The basic form of a stage

      %%{init: {"theme": "neutral"}}%%
      flowchart TD
         classDef style_plain fill:#ddd,stroke:#999
         classDef style_pre_stage fill:#fbb,stroke:#b77
         classDef style_begin_stage fill:#ede,stroke:#a9a
         classDef style_end_stage fill:#dfe,stroke:#9ba
         classDef style_post_stage fill:#fdc,stroke:#b98

         stage_entry(Stage Entry):::style_plain
         pre_stage_actions(Pre-Stage Actions):::style_pre_stage
         begin_stage_actions(Begin Stage Actions):::style_begin_stage
         stage_body(Stage Body):::style_plain
         end_stage_actions(End Stage Actions):::style_end_stage
         post_stage_actions(Post-Stage Actions):::style_post_stage
         stage_exit(Stage Exit):::style_plain

         stage_entry --> pre_stage_actions
         pre_stage_actions --> begin_stage_actions
         begin_stage_actions --> stage_body
         stage_body --> end_stage_actions
         end_stage_actions --> post_stage_actions
         post_stage_actions --> stage_exit

Conceptually speaking, any given stage has the following *phases*:

Pre-Stage Actions
    Anything that takes place before a stage actually begins.  E.g.,
    check that certain pre-conditions are met before proceeding.
Begin Stage Actions
    Whatever should happen at the beginning of the stage.  E.g., print
    or log some information for the user, capture timing information,
    etc.
Stage Body
    The actual work of the stage itself, which is entirely dependent on
    the script you're writing.
End Stage Actions
    Whatever should happen at the end of the stage.  E.g., print or log
    more information for the user, capture timing information, etc.
Post-Stage Actions
    Anything that takes place after a stage has finished.  E.g., check
    that certain post-conditions have been satisfied.

Depending on your script, some of these phases may be no-ops (e.g.,
pre-/post-stage actions), but conceptually they're all there.

Skipping Stages
---------------

If we want to get a bit fancier, we can include another phase for **Skip
Stage Actions**, which are whatever we want to do if we dynamically
decide to skip a stage.  Adding this feature changes the execution flow
to the following:

.. mermaid::

   %%{init: {"theme": "neutral"}}%%
   flowchart TD
      classDef style_plain fill:#ddd,stroke:#999
      classDef style_pre_stage fill:#fbb,stroke:#b77
      classDef style_begin_stage fill:#ede,stroke:#a9a
      classDef style_end_stage fill:#dfe,stroke:#9ba
      classDef style_post_stage fill:#fdc,stroke:#b98
      classDef style_skip_stage fill:#def,stroke:#9ab

      stage_entry(Stage Entry):::style_plain
      pre_stage_actions(Pre-Stage Actions):::style_pre_stage
      begin_stage_actions(Begin Stage Actions):::style_begin_stage
      execute_stage{{execute stage?}}:::style_plain
      stage_body(Stage Body):::style_plain
      skip_stage_actions(Skip Stage Actions):::style_skip_stage
      end_stage_actions(End Stage Actions):::style_end_stage
      post_stage_actions(Post-Stage Actions):::style_post_stage
      stage_exit(Stage Exit):::style_plain

      stage_entry --> pre_stage_actions
      pre_stage_actions --> begin_stage_actions
      begin_stage_actions --> execute_stage
      execute_stage -- Yes --> stage_body
      execute_stage -- No --> skip_stage_actions
      stage_body --> end_stage_actions
      skip_stage_actions --> end_stage_actions
      end_stage_actions --> post_stage_actions
      post_stage_actions --> stage_exit

Retrying Stages
---------------

If we want to get *even fancier*, we can allow for a stage to be
automatically retried.  Such flexibility is beneficial, because often
you're able to programmatically determine if something has gone wrong
during a stage.  In such circumstances, rather than requiring the user
to see the problem, decide what to do, and then act, you can design the
stage to automatically retry itself.  In that case, we add a **Retry
Stage Actions** phase, and the execution flow becomes the following:

.. mermaid::

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

      stage_entry(Stage Entry):::style_plain
      pre_stage_actions(Pre-Stage Actions):::style_pre_stage
      begin_stage_actions(Begin Stage Actions):::style_begin_stage
      execute_stage{{execute stage?}}:::style_plain
      stage_body(Stage Body):::style_plain
      skip_stage_actions(Skip Stage Actions):::style_skip_stage
      end_stage_actions(End Stage Actions):::style_end_stage
      retry_stage{{retry stage?}}:::style_retry_stage
      retry_stage_actions(Retry Stage Actions):::style_retry_stage
      post_stage_actions(Post-Stage Actions):::style_post_stage
      stage_exit(Stage Exit):::style_plain

      stage_entry --> pre_stage_actions
      pre_stage_actions --> begin_stage_actions
      begin_stage_actions --> execute_stage
      execute_stage -- Yes --> stage_body
      execute_stage -- No --> skip_stage_actions
      stage_body --> end_stage_actions
      skip_stage_actions --> end_stage_actions
      end_stage_actions --> retry_stage
      retry_stage -- Yes --> retry_stage_actions
      retry_stage_actions --> begin_stage_actions
      retry_stage -- No --> post_stage_actions
      post_stage_actions --> stage_exit

For details on how all the flexibility above is made available to the
user, see :doc:`stage-implementation-details`.
