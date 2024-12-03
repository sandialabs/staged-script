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
   :lines: 10-
   :emphasize-lines: 8-9,12-13,18-19
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
   :lines: 21-35
   :emphasize-lines: 15
   :caption: ``example/ex_6_creating_retryable_stages.py``

Next we'll add the flaky stage itself.  The keys here are raising the
:ref:`RetryStage <retry_stage_exception>` exception whenever you detect
something where a human would say, "Just try again," and setting
``self.script_success`` appropriately.

.. literalinclude:: ../../example/ex_6_creating_retryable_stages.py
   :language: python
   :linenos:
   :lines: 42-51
   :emphasize-lines: 7-8,10
   :caption: ``example/ex_6_creating_retryable_stages.py``

Next we need to adjust the parser to account for this new stage.

.. literalinclude:: ../../example/ex_6_creating_retryable_stages.py
   :language: python
   :linenos:
   :lines: 60-87
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
   :lines: 146-158
   :emphasize-lines: 6-9
   :caption: ``example/ex_7_customizing_the_summary.py``

In this case we're adding a new section to the summary with some details
about the machine the script was run on.  Now when we run just the first
stage, we see:

.. command-output:: python3 ../../example/ex_7_customizing_the_summary.py --some-file foo.txt --stage hello



Real-World Example:  System-Level Testing of a Kubernetes Application
---------------------------------------------------------------------

The `Geophysical Monitoring System`_ (GMS) is a suite of applications
that deploys via `Kubernetes`_.  The scripting to automatically run its
`system-level testing`_ on a cluster, as the applications would run in
production, was built up via a hierarchy of ``StagedScript`` subclasses:

.. _Geophysical Monitoring System:  https://github.com/SNL-GMS/GMS-PI25
.. _Kubernetes:  https://kubernetes.io/
.. _system-level testing:  https://github.com/SNL-GMS/GMS-PI25/tree/main/python/utils/gms_system_test

.. mermaid::

   %%{init: {"theme": "neutral"}}%%
   flowchart TD
      GMSSystemTest -. uses .-> IANSimDeploy
      GMSSystemTest -- includes a --> SimulatorMixin
      GMSSystemTest == is a ==> GMSKubeWrapper
      IANSimDeploy -- includes a --> SimulatorMixin
      IANSimDeploy == is a ==> GMSKubeWrapper
      SimulatorMixin -. uses .-> GMSKubeWrapper
      SimulatorMixin -. uses .-> StagedScript
      GMSKubeWrapper == is a ==> StagedScript

.. note::

   The links below use a prior version of the package.  Anywhere you see
   ``driver_script`` or ``DriverScript``, understand that those are
   essentially ``staged_script`` and ``StagedScript``.  There were a few
   breaking changes made in the midst of open-sourcing, but that
   shouldn't impact your ability to understand this example.

* |GMSKubeWrapper|_:  Instances of GMS are deployed to a cluster with
  the |gmskube|_ utility, which essentially just executes a series of
  `Helm`_ commands under the hood.  ``GMSKubeWrapper`` is a
  ``StagedScript`` that provides some stages for standard ``gmskube``
  commands.  It's not really intended to be run as a script by itself,
  though it could be; rather, it exists as a base class for more
  substantial scripts to inherit from.
* |SimulatorMixin|_:  To facilitate testing without live data, GMS
  includes a simulator that can be applied to a running instance of the
  system.  ``SimulatorMixin`` provides stages for interacting with the
  simulator.
* |IANSimDeploy|_:  One of the GMS applications is the Interactive
  Analysis (IAN) view.  ``IANSimDeploy`` is a ``StagedScript`` that
  allows both developers and CI services to deploy an instance of this
  application, with the simulator included, consistently.  It can be run
  as a script by itself, but also supplies some of its functionality to
  ``GMSSystemTest``.  The other GMS applications don't require their own
  specialized script for standing them up.
* |GMSSystemTest|_:  GMS' automated testing framework allows the user to
  stand up an instance of the system, run a series of tests against it,
  and then tear down the instance.  ``GMSSystemTest`` is a
  ``StagedScript`` that pulls everything together from all the other
  classes to make this happen.  It's primarily intended to be run in CI,
  though developers can run it locally as well to replicate exactly what
  happens in CI.

.. _GMSKubeWrapper:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py
.. |GMSKubeWrapper| replace::  ``GMSKubeWrapper``
.. _gmskube:  https://github.com/SNL-GMS/GMS-PI25/blob/main/doc/commands.md#gmskube
.. |gmskube| replace::  ``gmskube``
.. _Helm:  https://helm.sh/
.. _SimulatorMixin:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py
.. |SimulatorMixin| replace::  ``SimulatorMixin``
.. _IANSimDeploy:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/ian_sim_deploy/ian_sim_deploy/ian_sim_deploy.py
.. |IANSimDeploy| replace::  ``IANSimDeploy``
.. _GMSSystemTest:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py
.. |GMSSystemTest| replace::  ``GMSSystemTest``

The details of GMS and how it's deployed aren't important; rather, this
example showcases the flexibility of the framework provided by
``staged-script``.

Adding Stages
^^^^^^^^^^^^^

The stages provided by the classes are the following:

* ``GMSKubeWrapper``:

  * `install`_:  Stand up an instance of one of the GMS applications on
    a cluster.
  * `wait`_:  Wait for all the pods to reach a ready state.
  * `uninstall`_:  Tear down the instance.

* ``SimulatorMixin``:

  * `init`_:  Initialize the simulator.
  * `start`_:  Start data flowing.
  * `stop`_:  Stop the data flow.
  * `clean`_:  Clean up the simulator and return it to the uninitialized
    state.
  * `status`_:  Get the current status of the simulator.

* ``GMSSystemTest``:

  * `sleep`_:  Wait for some amount of time.  (This is historically
    present to overlook transient system instability.)
  * `test`_:  Run a `test augmentation`_ against the system and collect
    the results.

.. _install:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L150
.. _wait:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L168
.. _uninstall:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L200
.. _init:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py#L51
.. _start:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py#L71
.. _stop:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py#L85
.. _clean:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py#L95
.. _status:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py#L110
.. _sleep:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L327
.. _test:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L349
.. _test augmentation:  https://github.com/SNL-GMS/GMS-PI25/blob/main/deploy/augmentation/GMS_SUBCHART_README.md

Customizing the Parser
^^^^^^^^^^^^^^^^^^^^^^

The argument parser for ``GMSSystemTest`` is built up, bit by bit, by
the different classes.

* |GMSKubeWrapper adds|_:

  * ``--instance``:  The name of the GMS instance.
  * ``--save-logs``, ``--no-save-logs``:  Whether to save container logs
    before tearing everything down.
  * ``--log-dir``:  The directory in which to save container logs.
  * ``--tag``:  The container image tag to use.
  * ``--wait-timeout``:  How long to wait for the pods to reach a ready
    state.

* |IANSimDeploy adds|_:

  * ``--keycloak``, ``--no-keycloak``:  Whether to use KeyCloak
    authentication.
  * ``--node-env``:  Which Node environment to use (development or
    production).
  * ``--state-timeout``:  How long to wait for the simulator to
    transition between states.
  * A variety of options to pass on to the ``gmskube install`` command.
  * A variety of options for starting the simulator.

* |GMSSystemTest adds|_:

  * ``--type``:  Which of the GMS applications to stand up.
  * ``--sleep``:  How long to wait between the pods reaching the ready
    state and starting the test.
  * ``--test``:  Which test augmentation to apply to the system.
  * ``--env``:  Environment variables to set in the test environment.
  * ``--parallel``:  How many identical test augmentation pods to launch
    in parallel.

.. _GMSKubeWrapper adds:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L82
.. |GMSKubeWrapper adds| replace::  ``GMSKubeWrapper`` adds
.. _IANSimDeploy adds:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/ian_sim_deploy/ian_sim_deploy/ian_sim_deploy.py#L130
.. |IANSimDeploy adds| replace::  ``IANSimDeploy`` adds
.. _GMSSystemTest adds:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L158
.. |GMSSystemTest adds| replace::  ``GMSSystemTest`` adds

With all of these additions, if we run ``./gms_system_test.py --help``,
we see:

.. code-block::

   usage: gms_system_test.py [-h] [--stage {init,start,sleep,install,wait,test,uninstall} [{init,start,sleep,install,wait,test,uninstall} ...]]
                          [--dry-run] [--install-retry-attempts INSTALL_RETRY_ATTEMPTS] [--install-retry-delay INSTALL_RETRY_DELAY]
                          [--install-retry-timeout INSTALL_RETRY_TIMEOUT] [--test-retry-attempts TEST_RETRY_ATTEMPTS]
                          [--test-retry-delay TEST_RETRY_DELAY] [--test-retry-timeout TEST_RETRY_TIMEOUT] [--instance INSTANCE] [--log-dir LOG_DIR]
                          [--save-logs | --no-save-logs] [--tag TAG] [--wait-timeout WAIT_TIMEOUT] [--type {ian,keycloak,sb,logging}] [--sleep SLEEP]
                          [--test TEST] [--env ENV] [--parallel {1,2,3,4,5,6,7,8,9,10}] [--values VALUES]

   This script:
   * stands up a temporary instance of the GMS system,
   * waits for all the pods to be up and running,
   * sleeps a given amount of time to wait for the application to be ready,
   * runs a test augmentation against it, and
   * tears down the temporary instance after testing completes.

   Test augmentations, which run in a pod on a Kubernetes cluster, copy their test results to a MinIO test reporting service so that they can be gathered back to the machine on which this script was executed.  Final reports will be gathered in a ``gms_system_test-reports-{timestamp}-{unique-str}`` directory under the current working directory.  Additionally a ``gms_system_test-container-logs-{timestamp}-{unique-str}`` directory will contain logs from all the containers run as part of the testing.

   options:
     -h, --help            show this help message and exit
     --stage {init,start,sleep,install,wait,test,uninstall} [{init,start,sleep,install,wait,test,uninstall} ...]
                           Which stages to run. (default: {'init', 'start', 'sleep', 'install', 'wait', 'test', 'uninstall'})
     --dry-run             If specified, don't actually run the commands in the shell; instead print the commands that would have been executed.
                           (default: False)
     --instance INSTANCE   The name of the GMS instance. (default: None)
     --log-dir LOG_DIR     The directory in which to save the container logs. Defaults to `gms_system_test-container-logs-<timestamp>-<unique-str>`.
                           (default: None)
     --save-logs, --no-save-logs
                           Whether to save the container logs. (default: True)
     --tag TAG             Tag name, which corresponds to the docker tag of the images. The value entered will automatically be transformed according to
                           the definition of the gitlab `CI_COMMIT_REF_SLUG` variable definition (lowercase, shortened to 63 characters, and with
                           everything except `0-9` and `a-z` replaced with `-`, no leading / trailing `-`). (default: None)
     --wait-timeout WAIT_TIMEOUT
                           How long to wait (in seconds) for all the pods in the instance to be ready. (default: 900)
     --type {ian,keycloak,sb,logging}
                           The type of instance. (default: None)
     --sleep SLEEP         How long to wait between the pods reaching a 'Ready' state and starting the test. (default: 0)
     --test TEST           The name of a test to run (see ``gmskube augment catalog --tag <reference>``). (default: None)
     --env ENV             Set environment variables in the test environment. This argument can be specified multiple times to specify multiple values.
                           Example: ``--env FOO=bar`` will set ``FOO=bar`` for the test. (default: None)
     --parallel {1,2,3,4,5,6,7,8,9,10}
                           How many identical test augmentation pods to launch in parallel. (default: 1)

   retry:
     Additional options for retrying stages.

     --install-retry-attempts INSTALL_RETRY_ATTEMPTS
                           How many times to retry the 'install' stage. (default: 2)
     --install-retry-delay INSTALL_RETRY_DELAY
                           How long to wait (in seconds) before retrying the 'install' stage. (default: 0)
     --install-retry-timeout INSTALL_RETRY_TIMEOUT
                           How long to wait (in seconds) before giving up on retrying the 'install' stage. (default: 600)
     --test-retry-attempts TEST_RETRY_ATTEMPTS
                           How many times to retry the 'test' stage. (default: 5)
     --test-retry-delay TEST_RETRY_DELAY
                           How long to wait (in seconds) before retrying the 'test' stage. (default: 0)
     --test-retry-timeout TEST_RETRY_TIMEOUT
                           How long to wait (in seconds) before giving up on retrying the 'test' stage. (default: 1200)

   install:
     Additional options to pass on to ``gmskube install``.

     --values VALUES       Set override values in the chart using a YAML file. The chart `values.yaml` is always included first, existing values second
                           (for upgrade), followed by any override file(s). This file should only include the specific values you want to override; it
                           should not be the entire `values.yaml` from the chart. This flag can be used multiple times to specify multiple files. The
                           priority will be given to the last (right-most) file specified. (default: None)

   examples:
     Here are some standard use cases.

     Run the ``jest`` test against a ``sb`` instance deployed from the ``develop`` branch::

         gms_system_test.py --type sb --tag develop --test jest

     Verify that it's possible to install/uninstall ``ian``, but don't test anything::

         gms_system_test.py --type ian --tag develop --stage install wait init start uninstall

Customizing Stage Behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^

The transitions between the stages are customized as follows:

* ``GMSKubeWrapper``:

  * There are some `general pre-stage actions`_ defined (ensure we have
    an instance name, that the instance exists, and that we have a
    ``KubeCtl`` object ready to talk to it) that may be used by any
    number of stages defined here or in subclasses.
  * If the install stage fails, `uninstall the instance before retrying
    it`_.  If it still hasn't worked after the retries have been
    exhausted, `record the script failure and skip all future stages`_.
  * Before the wait stage, `run the general pre-stage actions`_.  If
    skipping this stage, `assume all the pods are ready`_.  If the pods
    aren't ready, `record the script failure`_.
  * Before the uninstall stage, `run the general pre-stage actions, and
    then save the container logs`_.

* ``SimulatorMixin``:  For each stage defined, |run the general
  pre-stage actions from GMSKubeWrapper|_.
* ``IANSimDeploy``:  If the pods aren't ready after the wait stage,
  `skip over all future stages`_.
* ``GMSSystemTest``:

  * Before the install stage, if an instance name wasn't supplied,
    `create a unique one`_.
  * If the pods aren't ready after the wait stage, `skip all future
    stages`_.
  * Before running the test stage, `ensure the instance tag is set, and
    create the test reports directory`_.  After it completes, `set the
    script success based on the test results`_.  If the tests fail,
    before retrying the stage, `save the container logs and clean things
    up`_.

.. _general pre-stage actions:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L436
.. _uninstall the instance before retrying it:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L409
.. _record the script failure and skip all future stages:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L426
.. _run the general pre-stage actions:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L458
.. _assume all the pods are ready:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L465
.. _record the script failure:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L473
.. _run the general pre-stage actions, and then save the container logs:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L482
.. _run the general pre-stage actions from GMSKubeWrapper:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/simulator_mixin/simulator_mixin/simulator_mixin.py#L345
.. |run the general pre-stage actions from GMSKubeWrapper| replace::  run the general pre-stage actions from ``GMSKubeWrapper``
.. _skip over all future stages:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/ian_sim_deploy/ian_sim_deploy/ian_sim_deploy.py#L400
.. _create a unique one:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L679
.. _skip all future stages:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L719
.. _ensure the instance tag is set, and create the test reports directory:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L729
.. _set the script success based on the test results:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L752
.. _save the container logs and clean things up:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L760

Customizing the Script Execution Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each class in the hierarchy can add details to the script execution
summary, to better communicate to users what was just run, and to ease
debugging of any failures, either locally or in CI.

* ``GMSKubeWrapper``:  `Adds the container logs directory and name of the
  current Kubernetes cluster`_.
* ``IANSimDeploy``:  `Adds the URL for the user interface`_, so users
  can quickly pull it up in their browser.
* ``GMSSystemTest``:  `Adds the test reports directory`_, so users can
  quickly see how things went.

.. _Adds the container logs directory and name of the current Kubernetes cluster:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/gmskube_wrapper/gmskube_wrapper/gmskube_wrapper.py#L215
.. _Adds the URL for the user interface:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/ian_sim_deploy/ian_sim_deploy/ian_sim_deploy.py#L332
.. _Adds the test reports directory:  https://github.com/SNL-GMS/GMS-PI25/blob/main/python/utils/gms_system_test/gms_system_test/gms_system_test.py#L419
