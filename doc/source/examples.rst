Examples
========

The following examples illustrate both the usage and the utility of
``staged-script``.  They build on each other in complexity, so it will
make the most sense to start here at the top and work your way down
through each in turn.



.. _the_basics:

The Basics
----------

We'll start with what amounts to a "Hello World" example, with two
simple stages to say "hello" and "goodbye".

.. literalinclude:: ../../example/ex_0_the_basics.py
   :language: python
   :linenos:
   :lines: 9-
   :emphasize-lines: 9-10,13-14,19-20
   :caption: ``example/ex_0_the_basics.py``

The two methods ``say_hello()`` and ``say_goodbye()`` are stand-ins for
whatever you might want to do in the stages of your script.  Note that
in this case they are simply :doc:`running commands in the underlying
shell <features/running-commands>`, but you could instead include
whatever Python code you want in here.

The ``main()`` method specifies the general form of the script, where
you first :doc:`parse the command line arguments
<features/dynamic-argument-parser>`, then try to execute a series of
stages (lines 20--21), and finally print the :doc:`script execution
summary <features/script-execution-summary>`, regardless of whether
anything went wrong in any of the stages.  You're welcome to construct
your scripts however you like---this general form is just a
recommendation.

Running the script, and passing the ``--help`` argument to it, yields
the following:

.. command-output:: python3 ../../example/ex_0_the_basics.py --help

If you tell it you only want to run the ``hello`` stage, you'll see

.. command-output:: python3 ../../example/ex_0_the_basics.py --stage hello

.. note::

   It's worth noting that ``StagedScript`` uses a
   ``rich.console.Console`` for all output, so you may want to
   familiarize yourself with the `Rich documentation`_ for the sake of
   customizing the ``StagedScript.console`` attribute.

.. _Rich documentation:  https://rich.readthedocs.io/



Customizing the Parser
----------------------

Removing the Retry Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a script as simple as this one, all of the retry business in the
help text and script execution summary are rather distracting, because
our two stages don't automatically retry themselves.  We can
:doc:`customize the argument parser <features/dynamic-argument-parser>`
by adding the following to the ``MyScript`` class:

.. literalinclude:: ../../example/ex_1_removing_the_retry_arguments.py
   :language: python
   :linenos:
   :lines: 27-39
   :caption: ``example/ex_1_removing_the_retry_arguments.py``

.. note::

   An upcoming release will refactor the retry argument attributes so
   `mypy`_ will be happy with them.  For now, just use the ``type:
   ignore[attr-defined]`` comments.

.. _mypy:  https://mypy-lang.org/

Now when we look at the ``--help`` text, we see:

.. command-output:: python3 ../../example/ex_1_removing_the_retry_arguments.py --help

This is much nicer from the user perspective.  Now if we run the script
with the same arguments as last time, we see:

.. command-output:: python3 ../../example/ex_1_removing_the_retry_arguments.py --stage hello

Running Certain Stages by Default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, a staged script won't run any stages unless you tell it to.
Keep in mind, this package was designed for improving replicability for
infrastructure automation, so we err on the side of `explicit is better
than implicit`_.  That said, you or your users may find this
inconvenient, and would prefer to make it such that certain stages run
by default when you don't specify ``--stage`` on the command line.  In
that case, you can add the highlighted line:

.. _explicit is better than implicit:  https://peps.python.org/pep-0020/

.. literalinclude:: ../../example/ex_2_running_certain_stages_by_default.py
   :language: python
   :linenos:
   :lines: 27-29,41-42
   :emphasize-lines: 4
   :caption: ``example/ex_2_running_certain_stages_by_default.py``

In this case I'm telling it to default the ``--stage`` argument to the
list of all the stages registered when instantiating a ``StagedScript``
subclass.  However, you could just as easily specify whatever subset of
stages you like here with, e.g., ``stage=["stage-1", "stage-2"]``.  Now,
if we run the script without any arguments, we see:

.. command-output:: python3 ../../example/ex_2_running_certain_stages_by_default.py

.. note::

   It's worth noting that the order of the stage names passed to the
   ``--stages`` argument on the command line does not affect the order
   in which the stages are run.  That is governed by the contents of the
   ``main()`` method, as shown in :ref:`the basic example <the_basics>`.

Adding Arguments
^^^^^^^^^^^^^^^^

Now let's see about adding some arguments to the parser beyond what
``StagedScript`` provides.  We can do this by adding arguments to the
:class:`python:argparse.ArgumentParser` as you normally would.

.. literalinclude:: ../../example/ex_3_adding_arguments.py
   :language: python
   :linenos:
   :lines: 32-34,45-57
   :emphasize-lines: 4-15
   :caption: ``example/ex_3_adding_arguments.py``

Beyond that, though, you likely also want to augment the parsing of the
arguments to handle these new options.  You can do so by extending the
:ref:`parse_args() <parse_args>` method provided by the base class.

.. literalinclude:: ../../example/ex_3_adding_arguments.py
   :language: python
   :linenos:
   :lines: 59-70
   :caption: ``example/ex_3_adding_arguments.py``

.. note::

   Here's we're taking the file the user gives us on the command line
   and resolving it to an absolute path.  This is again in service of
   improving replicability, as the script output will then point us
   directly to the exact file used at execution time, instead of just
   giving us a file name or relative path.

For the sake of using these new arguments in our script, let's modify
the two stages to take them into account.

.. literalinclude:: ../../example/ex_3_adding_arguments.py
   :language: python
   :linenos:
   :lines: 20-30
   :emphasize-lines: 4,10
   :caption: ``example/ex_3_adding_arguments.py``

Now if we run the script, passing in a file on the command line, we see:

.. command-output:: python3 ../../example/ex_3_adding_arguments.py --some-file foo.txt



Customizing Stage Behavior
--------------------------

For All Stages
^^^^^^^^^^^^^^

We now move beyond customizing the parser to adjusting the behavior of
the stages as they run.  Recall from
:doc:`features/the-conceptual-stage` that a stage is broken down into a
number of phases, each of which has a corresponding method.  These phase
methods have reasonable :ref:`default implementations
<stage_customization>` in the base class, but may be extended or
overridden in your subclasses.

.. literalinclude:: ../../example/ex_4_customizing_stage_behavior.py
   :language: python
   :linenos:
   :lines: 72-93
   :caption: ``example/ex_4_customizing_stage_behavior.py``

.. note::

   The ``_begin_stage()`` method is not included above, meaning it is
   neither extended nor overridden, so the base class implementation
   will be used.

Now when we run the script, we can see the changed behavior:

.. command-output:: python3 ../../example/ex_4_customizing_stage_behavior.py --some-file foo.txt --some-flag --stage goodbye

You're free to customize the phases of the stage however you like, but
generally speaking the phases are useful for doing the following:

+---------------------+---------------------------------------------+
| Phase               | Actions                                     |
+=====================+=============================================+
| Pre-Stage Actions   | Checking pre-conditions and erroring        |
|                     | appropriately if not met                    |
+---------------------+---------------------------------------------+
| Begin Stage Actions | Telling the user what's about to happen and |
|                     | capturing state                             |
+---------------------+---------------------------------------------+
| Skip Stage Actions  | Telling the user what's happening and why   |
+---------------------+---------------------------------------------+
| End Stage Actions   | Capturing state; potentially displaying     |
|                     | information                                 |
+---------------------+---------------------------------------------+
| Post-Stage Actions  | Checking post-conditions and erroring       |
|                     | appropriately if not met                    |
+---------------------+---------------------------------------------+

For Individual Stages
^^^^^^^^^^^^^^^^^^^^^

In addition to tweaking the phase implementations for all stages, you
also have the flexibility to :ref:`tailor things on a stage-by-stage
basis <stage_customization>`.  This can be particularly helpful, e.g.,
in the **Pre-** and **Post-Stage Actions** for checking the pre- and
post-conditions specific to each stage.  To customize a phase method for
a particular stage, you just need to define a phase method as before,
but then append ``_STAGE_NAME`` to the method name, where ``STAGE_NAME``
is the name of the stage as provided to the :ref:`StagedScript.stage()
<the_stage_decorator>` decorator.

.. literalinclude:: ../../example/ex_5_customizing_individual_stages.py
   :language: python
   :linenos:
   :lines: 95-112
   :caption: ``example/ex_5_customizing_individual_stages.py``

Now when we run both stages we see:

.. command-output:: python3 ../../example/ex_5_customizing_individual_stages.py --some-file foo.txt

For Retryable Stages
^^^^^^^^^^^^^^^^^^^^

Now that we're familiar with the process of customizing stage behavior,
we can move on to introducing a retryable phase.  For demonstration
purposes, we'll simply add a stage that fails twice before it passes,
but in reality you would want to check on how things went when executing
a particular stage, and if something happens where a human would look at
it and say, "Yes, I understand what happened here; we just need to try
again and it should pass," you can program that logic into the stage
itself.

.. warning::

   You don't want to use this feature to hide problems with your actual
   code base.  If there's flakiness in your application or
   infrastructure that's *your fault*, you want those problems in your
   face to incentivize fixing them.  However, if there's flakiness due
   to various things outside your control (e.g., corporate or external
   infrastructure that may be unreachable from time to time), this can
   be a helpful way of hiding such problems from your team and avoiding
   the "everyone hates CI because it randomly fails" problem.

There's a good deal to add to our script at this point, so let's walk
through the pieces one at a time.  First we'll add an ``__init__()``
method, but that's just so we can keep track of the number of times our
flaky stage has been run.

.. literalinclude:: ../../example/ex_6_creating_retryable_stages.py
   :language: python
   :linenos:
   :lines: 20-34
   :emphasize-lines: 15
   :caption: ``example/ex_6_creating_retryable_stages.py``

Next we'll add the flaky stage itself.  The keys here are raising the
:ref:`RetryStage <retry_stage_exception>` exception whenever you detect
something where a human would say, "Just try again," and setting
``self.script_success`` appropriately.

.. literalinclude:: ../../example/ex_6_creating_retryable_stages.py
   :language: python
   :linenos:
   :lines: 41-50
   :emphasize-lines: 7-8,10
   :caption: ``example/ex_6_creating_retryable_stages.py``

Next we need to adjust the parser to account for this new stage.

.. literalinclude:: ../../example/ex_6_creating_retryable_stages.py
   :language: python
   :linenos:
   :lines: 59-86
   :emphasize-lines: 13-14
   :caption: ``example/ex_6_creating_retryable_stages.py``

Note that we've removed the lines

.. code-block:: python

   self.retry_arg_group.title = argparse.SUPPRESS
   self.retry_arg_group.description = argparse.SUPPRESS

so that when we look at the help text, we see:

.. command-output:: python3 ../../example/ex_6_creating_retryable_stages.py --help

Now when we run all the stages, we see:

.. command-output:: python3 ../../example/ex_6_creating_retryable_stages.py --some-file foo.txt

Note that it took three tries before the flaky stage finally passed.
If, however, the user is impatient and doesn't want to retry the stage,
we'd see:

.. command-output:: python3 ../../example/ex_6_creating_retryable_stages.py --some-file foo.txt --flaky-retry-attempts 0

Note that the flaky stage ran only once, and the script tells us of the
overall failure at the end of the summary.

.. note::

   The default retry behavior is governed by the :ref:`retry phase
   methods <customizing_retry_behavior>`, which can be customized like
   any other phase methods in the same way as demonstrated above.  The
   retry behavior is handled by ``tenacity.Retrying``, so you might want
   to familiarize yourself with the `Tenacity documentation`_.

.. _Tenacity documentation:  https://tenacity.readthedocs.io/



Customizing the Script Execution Summary
----------------------------------------

The purpose of the script execution summary is to give the user an
overview of what happened while the script was running, providing
sufficient details for them or their teammates to replicate what was run
and ease any debugging that may be necessary.  By default,
``StagedScript`` provides all the details you've seen in the examples
above, but you have the flexibility to :ref:`extend the behavior
<script_execution_summary>` for your subclasses.

.. literalinclude:: ../../example/ex_7_customizing_the_summary.py
   :language: python
   :linenos:
   :lines: 145-157
   :emphasize-lines: 6-9
   :caption: ``example/ex_7_customizing_the_summary.py``

In this case we're adding a new section to the summary with some details
about the machine the script was run on.  Now when we run just the first
stage, we see:

.. command-output:: python3 ../../example/ex_7_customizing_the_summary.py --some-file foo.txt --stage hello
