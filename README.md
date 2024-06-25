![Lines of code](https://sloc.xyz/github/sandialabs/staged-script/?category=code)
[![codecov](https://codecov.io/gh/sandialabs/staged-script/branch/master/graph/badge.svg?token=FmDStZ6FVR)](https://codecov.io/gh/sandialabs/staged-script)
[![CodeFactor](https://www.codefactor.io/repository/github/sandialabs/staged-script/badge/master)](https://www.codefactor.io/repository/github/sandialabs/staged-script/overview/master)
[![CodeQL](https://github.com/sandialabs/staged-script/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/sandialabs/staged-script/actions/workflows/github-code-scanning/codeql)
[![Conda Version](https://img.shields.io/conda/v/conda-forge/staged-script?label=conda-forge)](https://anaconda.org/conda-forge/staged-script)
![Conda Downloads](https://img.shields.io/conda/d/conda-forge/staged-script?label=conda-forge%20downloads)
[![Continuous Integration](https://github.com/sandialabs/staged-script/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/sandialabs/staged-script/actions/workflows/continuous-integration.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![GitHub contributors](https://img.shields.io/github/contributors/sandialabs/staged-script.svg)](https://github.com/sandialabs/staged-script/graphs/contributors)
[![Documentation Status](https://readthedocs.org/projects/staged-script/badge/?version=latest)](https://staged-script.readthedocs.io/en/latest/?badge=latest)
[![License](https://anaconda.org/conda-forge/staged-script/badges/license.svg)](LICENSE.md)
[![Merged PRs](https://img.shields.io/github/issues-pr-closed-raw/sandialabs/staged-script.svg?label=merged+PRs)](https://github.com/sandialabs/staged-script/pulls?q=is:pr+is:merged)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/8864/badge)](https://bestpractices.coreinfrastructure.org/projects/8864)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/sandialabs/staged-script/badge)](https://securityscorecards.dev/viewer/?uri=github.com/sandialabs/staged-script)
![Platforms](https://anaconda.org/conda-forge/staged-script/badges/platforms.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci Status](https://results.pre-commit.ci/badge/github/sandialabs/staged-script/master.svg)](https://results.pre-commit.ci/latest/github/sandialabs/staged-script/master)
[![PyPI - Version](https://img.shields.io/pypi/v/staged-script?label=PyPI)](https://pypi.org/project/staged-script/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/staged-script?label=PyPI%20downloads)
![Python Version](https://img.shields.io/badge/Python-3.8|3.9|3.10|3.11|3.12-blue.svg)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# staged-script

Python is an ideal language for certain types of infrastructure automation.
Automating what a user does manually often involves walking through a series of
stages.  A user may wish to run all the stages in series, or perhaps only a
subset, and depending on how things go, certain stages may need to be retried.
Once the script finishes running, it'd be ideal if it could tell the user
exactly what was run, for the sake of easing replicability.  `staged-script`
aims to ease the development such automation scripts.  It's easy to get started
with, but also provides significant power-user functionality for those who need
it.

## Installation

To get up and running with `staged-script`, simply:
```bash
python3 -m pip install staged-script
```

## Usage

Once installed, you can simply
```python
import sys
from typing import List

from staged_script import StagedScript


class MyScript(StagedScript):

    @StagedScript.stage("hello", "Greeting the user")
    def say_hello(self) -> None:
        self.run("echo 'Hello World'", shell=True)

    @StagedScript.stage("goodbye", "Bidding farewell")
    def say_goodbye(self) -> None:
        self.run("echo 'Goodbye World'", shell=True)

    def main(self, argv: List[str]) -> None:
        self.parse_args(argv)
        try:
            self.say_hello()
            self.say_goodbye()
        finally:
            self.print_script_execution_summary()


if __name__ == "__main__":
    my_script = MyScript({"hello", "goodbye"})
    my_script.main(sys.argv[1:])
```

For more detailed usage and API information, please see
[our documentation][docs].

[docs]: https://staged-script.readthedocs.io

## Where to Get Help

If you're having trouble with `staged-script`, or just want to ask a question,
head on over to [our issue board][issues].  If a quick search doesn't yield
what you're looking for, feel free to file an issue.

[issues]: https://github.com/sandialabs/staged-script/issues

## Contributing

If you're interested in contributing to the development of `staged-script`,
we'd love to have your help :grinning:  Check out our
[contributing guidelines](CONTRIBUTING.md) for how to get started.
[Past contributors][contributors] include:
* [@jmgate](https://github.com/jmgate)

[contributors]: https://github.com/sandialabs/staged-script/graphs/contributors

## License

See [LICENSE.md](LICENSE.md).

## Credits

Special thanks to [the GMS project][gms] for investing in the development of
this package.  Aspects of this functionality were inspired by the
[SPiFI][spifi] Jenkins Pipeline plugin and the [ShellLogger][shelllogger]
Python package.

[gms]: https://github.com/SNL-GMS/GMS-PI25
[spifi]: https://github.com/sandialabs/SPiFI
[shelllogger]: https://github.com/sandialabs/shell-logger
