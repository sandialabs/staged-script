|Code lines|
|codecov|
|CodeFactor|
|CodeQL|
|conda-forge Version|
|conda-forge Downloads|
|Continuous Integration|
|Contributor Covenant|
|GitHub Contributors|
|Documentation Status|
|License|
|Merged PRs|
|OpenSSF Best Practices|
|OpenSSF Scorecard|
|Platforms|
|pre-commit|
|pre-commit.ci Status|
|PyPI Version|
|PyPI Downloads|
|Python Version|
|Ruff|

.. |Code lines| image:: https://sloc.xyz/github/sandialabs/staged-script/?category=code
.. |codecov| image:: https://codecov.io/gh/sandialabs/staged-script/branch/master/graph/badge.svg?token=FmDStZ6FVR
   :target: https://codecov.io/gh/sandialabs/staged-script
.. |CodeFactor| image:: https://www.codefactor.io/repository/github/sandialabs/staged-script/badge/master
   :target: https://www.codefactor.io/repository/github/sandialabs/staged-script/overview/master
.. |CodeQL| image:: https://github.com/sandialabs/staged-script/actions/workflows/github-code-scanning/codeql/badge.svg
   :target: https://github.com/sandialabs/staged-script/actions/workflows/github-code-scanning/codeql
.. |conda-forge Version| image:: https://img.shields.io/conda/v/conda-forge/staged-script?label=conda-forge
   :target: https://anaconda.org/conda-forge/staged-script
.. |conda-forge Downloads| image:: https://img.shields.io/conda/d/conda-forge/staged-script?label=conda-forge%20downloads
.. |Continuous Integration| image:: https://github.com/sandialabs/staged-script/actions/workflows/continuous-integration.yml/badge.svg
   :target: https://github.com/sandialabs/staged-script/actions/workflows/continuous-integration.yml
.. |Contributor Covenant| image:: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg
   :target: https://github.com/sandialabs/staged-script/blob/master/CODE_OF_CONDUCT.md
.. |GitHub Contributors| image:: https://img.shields.io/github/contributors/sandialabs/staged-script.svg
   :target: https://github.com/sandialabs/staged-script/graphs/contributors
.. |Documentation Status| image:: https://readthedocs.org/projects/staged-script/badge/?version=latest
   :target: https://staged-script.readthedocs.io/en/latest/?badge=latest
.. |License| image:: https://anaconda.org/conda-forge/staged-script/badges/license.svg
   :target: https://github.com/sandialabs/staged-script/blob/master/LICENSE.md
.. |Merged PRs| image:: https://img.shields.io/github/issues-pr-closed-raw/sandialabs/staged-script.svg?label=merged+PRs
   :target: https://github.com/sandialabs/staged-script/pulls?q=is:pr+is:merged
.. |OpenSSF Best Practices| image:: https://bestpractices.coreinfrastructure.org/projects/8864/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/8864
.. |OpenSSF Scorecard| image:: https://api.securityscorecards.dev/projects/github.com/sandialabs/staged-script/badge
   :target: https://securityscorecards.dev/viewer/?uri=github.com/sandialabs/staged-script
.. |Platforms| image:: https://anaconda.org/conda-forge/staged-script/badges/platforms.svg
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit
.. |pre-commit.ci Status| image:: https://results.pre-commit.ci/badge/github/sandialabs/staged-script/master.svg
   :target: https://results.pre-commit.ci/latest/github/sandialabs/staged-script/master
.. |PyPI Version| image:: https://img.shields.io/pypi/v/staged-script?label=PyPI
   :target: https://pypi.org/project/staged-script/
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/staged-script?label=PyPI%20downloads
.. |Python Version| image:: https://img.shields.io/badge/Python-3.9|3.10|3.11|3.12|3.13-blue.svg
.. |Ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff

staged-script
=============

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   motivation
   features
   examples
   reference

Python is an ideal language for certain types of infrastructure
automation.  Automating what a user does manually often involves walking
through a series of stages.  A user may wish to run all the stages in
series, or perhaps only a subset, and depending on how things go,
certain stages may need to be retried.  Once the script finishes
running, it'd be ideal if it could tell the user exactly what was run,
for the sake of easing replicability.  ``staged-script`` aims to ease
the development such automation scripts.  It's easy to get started with,
but also provides significant power-user functionality for those who
need it.

Installation
------------

To get up and running with ``staged-script``, simply

.. code-block:: bash

   python3 -m pip install staged-script

Usage
-----

Once the package is installed, you can simply

.. literalinclude:: ../../example/ex_0_the_basics.py
   :language: python
   :linenos:
   :lines: 10-
   :caption: ``example/ex_0_the_basics.py``

For more detailed usage information, see the :doc:`examples` page.  For
implementation details, see the :doc:`reference` documentation.

Contributing
------------

The source repository for this module is `on GitHub`_.  See the
project's README and contributing guidelines for details on how to
interact with the project.

.. _on GitHub:  https://github.com/sandialabs/staged-script

Inspiration
-----------

Aspects of this functionality were inspired by the `SPiFI`_ Jenkins
Pipeline plugin and the `shell-logger`_ Python package.

.. _SPiFI:  https://github.com/sandialabs/SPiFI
.. _shell-logger:  https://github.com/sandialabs/shell-logger
