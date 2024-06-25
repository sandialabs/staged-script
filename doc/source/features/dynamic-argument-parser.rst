Dynamic ArgumentParser
======================

``staged-script`` provides :ref:`parsing methods <parsing_arguments>` to
construct an :class:`python:argparse.ArgumentParser` and then use it in
parsing the command line arguments passed to your script.  What's
provided in the base class only provides and parses arguments specific
to :ref:`StagedScript <the_stagedscript_class>` itself, but it's
intended to be extended by subclasses.  The usage of the
:func:`python:functools.cached_property` decorator under the hood means
the subclass ``parser`` will be evaluated, and unrolled, when it's first
used.

.. note::

   This even allows for the creation of a complex hierarchy of
   ``StagedScript`` derivatives, where each class's ``parser()`` and
   ``parse_args()`` methods extend the corresponding methods of its
   parent.

The base class provides the following arguments:

* ``--stage``:  Which stages to run.  The available choices are
  automatically populated by the stages defined in the subclass.
* For each stage defined:

  * ``--STAGE-retry-attempts``:  How many times to retry the stage.
  * ``--STAGE-retry-delay``:  How long to delay before retrying.
  * ``--STAGE-retry-timeout``:  How long before giving up.

  .. note::

     These arguments are also captured in class attributes, in case
     subclass developers want to modify them (e.g., suppress them when
     they're not applicable).

* ``--dry-run``:  Don't actually run commands, just print them.
