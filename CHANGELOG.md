# CHANGELOG



## v2.0.3 (2025-06-09)

### Patch
* patch: Sign release commits and tags ([`4f2caa1`](https://github.com/sandialabs/staged-script/commit/4f2caa191e797e8dad7f2d7cda6511c70feb458c))

## v2.0.2 (2025-05-27)

### Chores
* chore: Update security notice ([`b101953`](https://github.com/sandialabs/staged-script/commit/b1019531ebf745d03a97345b3bc2bc7c618c7cb3))

  The Best Practices Badge App suggests we should document what users can
  expect from our project in terms of security.

### Code style
* style: Sort imports ([`3dd62ec`](https://github.com/sandialabs/staged-script/commit/3dd62ecc5f0df1fe7ef2f87b42eff882006c880d))

  Discovered by ruff:

  staged_script/__init__.py:21:11: RUF022 [*] `__all__` is not sorted
     |
  19 | )
  20 |
  21 | __all__ = [
     | ___________^
  22 | | "StagedScript",
  23 | | "HelpFormatter",
  24 | | "RetryStage",
  25 | | "StageDuration",
  26 | | ]
     | |_^ RUF022
  27 | __version__ = "2.0.0"
     |
     = help: Apply an isort-style sorting to `__all__`

### Continuous integration
* ci: Replace deprecated GitHub Action ([`a300200`](https://github.com/sandialabs/staged-script/commit/a300200df4e97081e9022b2b58dc22f923b639c7))

### Documentation
* docs: Switch to `project_copyright` ([`43f1d31`](https://github.com/sandialabs/staged-script/commit/43f1d312f4dd6c2f56b58869c31ff91af0cabd4f))

  Using this alias means we're no longer overshadowing the `copyright`
  built-in, so we can remove the comment to ignore that Ruff linting rule.

### Patch
* patch: Omit auto-updates from CHANGELOG ([`a61c6ea`](https://github.com/sandialabs/staged-script/commit/a61c6eac599efdc55e0aeeebdd92d2189a89f6a5))

### Refactoring
* refactor: Fix issues from ruff-pre-commit update ([`ecce915`](https://github.com/sandialabs/staged-script/commit/ecce91522352f43f3b5163ca3b0977b7dcb5d8c1))

## v2.0.1 (2024-12-17)

### Patch
* patch: Support Python 3.13 ([`c0a242c`](https://github.com/sandialabs/staged-script/commit/c0a242c8c3a1866aff0c923c0088a602b51b8350))

## v2.0.0 (2024-12-03)

### Chores
* chore!: Drop support for Python 3.8 ([`a9c8005`](https://github.com/sandialabs/staged-script/commit/a9c80052734c44f8d25bbce7599b315ac627c639))

  * Use type-hinting provided out of the box in 3.9.
  * Use new dictionary update syntax.
  * Update the docs and CI accordingly.
* chore: Group dependabot updates ([`aef5ea5`](https://github.com/sandialabs/staged-script/commit/aef5ea52cb2145382554b5c2bc600f1e261bcb7c))

  Run dependabot updates weekly instead of daily, and group them together
  for the different providers (GitHub Actions and pip), to reduce the
  amount of noise in the repository history.
* chore(deps): No longer pin Sphinx version ([`21d0cc4`](https://github.com/sandialabs/staged-script/commit/21d0cc41327fb678979c9ac40d382da987d2037a))

  sphinx-rtd-theme has been updated to work with the latest Sphinx
  version.
* chore(deps): Update sphinx requirement from <8.0.0 to <9.0.0 ([`b554db0`](https://github.com/sandialabs/staged-script/commit/b554db0ebce52fdc769d707d54cd28432167433e))

  Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
  - [Release notes](https://github.com/sphinx-doc/sphinx/releases)
  - [Changelog](https://github.com/sphinx-doc/sphinx/blob/v8.1.3/CHANGES.rst)
  - [Commits](https://github.com/sphinx-doc/sphinx/compare/v0.1.61611...v8.1.3)

  ---
  updated-dependencies:
  - dependency-name: sphinx
    dependency-type: direct:production
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore: Update LICENSE/COPYRIGHT files ([`bcf3433`](https://github.com/sandialabs/staged-script/commit/bcf34339f29b1da38553d3477220f7a05a3603b1))
* chore: Change license title ([`6d30b36`](https://github.com/sandialabs/staged-script/commit/6d30b365b7dcd41d520e693616d97e1bcaa1a3ac))

  Try updating the title of the LICENSE.md file to see if that fixes
  https://github.com/sandialabs/staged-script/security/code-scanning/33.

### Continuous integration
* ci: Fix typo ([`bd4d832`](https://github.com/sandialabs/staged-script/commit/bd4d832ac728fec0aa8bcea43d54ff51a2b492e4))

  Should have been included in 627a50ffc2dbbe20303b9f50a9b186eb4bf2cd1b.
* ci: Restrict CI permissions to read ([`627a50f`](https://github.com/sandialabs/staged-script/commit/627a50ffc2dbbe20303b9f50a9b186eb4bf2cd1b))

  https://github.com/sandialabs/staged-script/security/code-scanning/20
* ci: Change documentation coverage file name ([`35c39d8`](https://github.com/sandialabs/staged-script/commit/35c39d8b15f501a5f7ff834fd817ad284192e1d7))
* ci: Tweak automated suggestions ([`0f0b3d3`](https://github.com/sandialabs/staged-script/commit/0f0b3d3afacfb7e7eb5eb65d6420d5ee690295ce))
* ci: Apply security best practices ([`5a2ca31`](https://github.com/sandialabs/staged-script/commit/5a2ca31ff21a4eee3029cd9357c8957ad544577c))

  Signed-off-by: StepSecurity Bot <bot@stepsecurity.io>

### Documentation
* docs: Add real-world example ([`30bd774`](https://github.com/sandialabs/staged-script/commit/30bd774c24fd80ac3c49ee0183a5fa637913714e))

  Include the GMS system-level testing class hierarchy as an example of
  the significant flexibility afforded by the `staged-script` framework.
* docs: Pin Sphinx version ([`3a1c80d`](https://github.com/sandialabs/staged-script/commit/3a1c80ddf47d6ab7bbdacc3f2153ddda525d19d9))

  The Sphinx 8.0.0 release causes problems with sphinx-rtd-theme, so I'm
  pinning Sphinx below 8.0 to get things back up and running again.
* docs: Fix lines included from examples ([`8dd8fb4`](https://github.com/sandialabs/staged-script/commit/8dd8fb4a9be354aa50291f172bc8d4b231437104))

  Should have been included in ccfa0d9a6cb7428d4ba4c7e38f7d07d02efe9a8c.

### Testing
* test: Remove unnecessary parentheses ([`b190ac6`](https://github.com/sandialabs/staged-script/commit/b190ac652233acb1fb8f289115df4c9086cd4947))

  To align with updated ruff rules.

## v1.0.2 (2024-07-02)

### Bug fixes
* fix: Specify Poetry dependencies ([`d3e3b5c`](https://github.com/sandialabs/staged-script/commit/d3e3b5cfee191a2694793b9c06355ba441a839c5))

## v1.0.1 (2024-07-02)

### Chores
* chore: Add CHANGELOG ([`c5ce0f4`](https://github.com/sandialabs/staged-script/commit/c5ce0f4fef72f87b3db7fb625fd2c1ed672daf9d))

  Add a dummy CHANGELOG.md to be overwritten by Semantic Release.
* chore: Add example requirements ([`343b8e7`](https://github.com/sandialabs/staged-script/commit/343b8e73ebb55afd3778df55e4b2e626b4e0e3b1))

  Add a blank requirements file for the examples to facilitate adding
  requirements in the future.

### Continuous integration
* ci: Omit `--fix` arg ([`2207516`](https://github.com/sandialabs/staged-script/commit/2207516f73beb88a734609de63f614553e4d334b))

  When running `ruff` via pre-commit, don't automatically fix the
  problems; instead tell the user what's wrong to train them into not
  making the problems in the first place.
* ci: Add semantic release templates ([`0cb13c1`](https://github.com/sandialabs/staged-script/commit/0cb13c1ed77d364a42c425352050358e8614d494))

  Add templates for the release notes and `CHANGELOG` so
  `python-semantic-release` can generate these files correctly in CI.
* ci: Check documentation spelling and coverage ([`e5b3719`](https://github.com/sandialabs/staged-script/commit/e5b3719a6eebed28675179085b06848e0c779b47))
* ci: Add semantic release workflow ([`7725e5e`](https://github.com/sandialabs/staged-script/commit/7725e5ecee269fb37a6697d3dfc1f60acb651ea8))

### Documentation
* docs: Slight tweaks to contributing guidelines ([`59325de`](https://github.com/sandialabs/staged-script/commit/59325de02308bef0e82a4c0e1e0c80363b67802b))

### Patch
* patch: Indicate that the package is typed ([`55a20c9`](https://github.com/sandialabs/staged-script/commit/55a20c9f70c296643496e0091551055176ef9676))

  According to PEP 561, we need to add this file to static type checkers
  can infer the types from the package.

### Testing
* test: Run the examples and check their output ([`ccfa0d9`](https://github.com/sandialabs/staged-script/commit/ccfa0d9a6cb7428d4ba4c7e38f7d07d02efe9a8c))

## v1.0.0 (2024-06-25)

### Bug fixes
* fix: Retry group help text ([`d237e38`](https://github.com/sandialabs/staged-script/commit/d237e38f8e9a76e3a1f3eac9e7a7470bc0ccc7e2))

  When I created the retry group in the argument parser, I didn't realize
  that I was using `add_argument_group` in a way in which it wasn't
  intended to be used. This commit brings things into conformity with
  how `argparse` is intended to be used, specifying a one-word group name,
  followed by a more detailed group description.
* fix!: Handle --dry-run correctly ([`8f436af`](https://github.com/sandialabs/staged-script/commit/8f436af8529623ce8e0f929aaae191c670d444a1))

  When a `DriverScript` subclass is run in dry-run mode, instead of
  executing commands in the shell, print a message indicating what would
  have been run. Prior to this, `DriverScript` provided the flag, but
  relied on subclass developers to ensure commands weren't run. This was
  an oversight.

  Note that this is a breaking change, as behavior of the `run()` method
  has fundamentally changed for dry-run mode.

### Chores
* chore: Update .gitignore ([`815c8cd`](https://github.com/sandialabs/staged-script/commit/815c8cdabe0ef7e89584f5eb395758c51a7f4a4e))
* chore: Ignore mypy warnings ([`4dbf516`](https://github.com/sandialabs/staged-script/commit/4dbf516b868d68471e7eb0e79d835b832743d6a2))

  Temporarily disable these warnings until there's time to revisit and
  address them.
* chore: Add version to __init__.py ([`f42f22d`](https://github.com/sandialabs/staged-script/commit/f42f22d4a8e2dc553ffe2ec0df039078ffb45772))
* chore: Remove YAPF comments ([`86f5cfe`](https://github.com/sandialabs/staged-script/commit/86f5cfeb2886f25a3cef9dd7035e635748038a9d))

  No longer needed after switching from YAPF to Ruff.
* chore: Ignore mypy warnings ([`a21b0c2`](https://github.com/sandialabs/staged-script/commit/a21b0c26ffd5007dc0cc42c1914ca3fc1f41382b))

  Temporarily disable these warnings until there's time to revisit and
  address them.
* chore: Ignore unchecked shell input ([`520b68e`](https://github.com/sandialabs/staged-script/commit/520b68e18c7e492ecec529d4d0a64e2f04b180af))

  When we built the precursor to `staged-script`, we didn't understand the
  security implications of having the user pass commands to the underlying
  shell as a string rather than a list of strings. It just seemed like a
  better interface, to make it easy for the user writing their Python
  scripts to simply wrap their bash commands. However, this opens up a
  danger for bad actors to cause problems via command injection. We can
  remove the vulnerability by switching to only allowing a list of strings
  as input to `run()`, but that breaking change will need to wait till
  another day when I have more time available.
* chore: Use installed reverse_argparse ([`7a3d1b7`](https://github.com/sandialabs/staged-script/commit/7a3d1b734a40acd92b2c8d05f04fb21489681644))
* chore: Move __init__.py ([`ba94a17`](https://github.com/sandialabs/staged-script/commit/ba94a171396fc05795e9aa9dd7fa372aac34ee49))
* chore: Remove unnecessary shebang lines ([`3516d84`](https://github.com/sandialabs/staged-script/commit/3516d846d50894d6cec9d6365bd6a807c566596c))
* chore: Add requirements files ([`0dc5512`](https://github.com/sandialabs/staged-script/commit/0dc5512f072c9da26506fb3107ae244f38188a10))
* chore: Add pyproject.toml ([`e81f2d2`](https://github.com/sandialabs/staged-script/commit/e81f2d269b93ca7d2b08553728c7d479e43c5468))
* chore: Add GitHub issur/PR templates ([`017b544`](https://github.com/sandialabs/staged-script/commit/017b5444c285159dddd48fa2b91f77ac77c2c4e6))

### Code style
* style: Automatically format the code base ([`2413186`](https://github.com/sandialabs/staged-script/commit/241318690718a23368af69680e347b02b4a2062d))
* style: Pytest parametrize tuple ([`0211644`](https://github.com/sandialabs/staged-script/commit/02116440f957c59f77f008dc461371788dc0f1ce))
* style: Match exception message ([`c2353bd`](https://github.com/sandialabs/staged-script/commit/c2353bd1fa327ddc2e5e0e317c80a755493f9cff))
* style: User iterable unpacking ([`9b18fac`](https://github.com/sandialabs/staged-script/commit/9b18fac70182c84d7d26bb9ae2aa8840dd03c981))
* style: Use f-string conversion flag ([`56b2c45`](https://github.com/sandialabs/staged-script/commit/56b2c4509bf29de11313b2c03c9d89d011389975))

### Continuous integration
* ci: Add ReadTheDocs configuration ([`40f08f2`](https://github.com/sandialabs/staged-script/commit/40f08f2c8a52e1181ca7b8ae473754abcfd54bf1))
* ci: Don't fail fast ([`0d3a5e3`](https://github.com/sandialabs/staged-script/commit/0d3a5e3a2a1b41d8dc11a3c7b7ec2a4a67c9fd98))

  If one job in the matrix of jobs fails, we still want to be able to see
  the results from the other jobs.
* ci: Stub out workflow ([`c2ab413`](https://github.com/sandialabs/staged-script/commit/c2ab4134bc2f53dd502e6df5996a7f0ad3d06931))
* ci: Add OpenSSF Scorecard workflow ([`f2904b7`](https://github.com/sandialabs/staged-script/commit/f2904b7318c3874a1b2694bb5085b63c8a0c7179))
* ci: Add pre-commit configuration ([`d4823f4`](https://github.com/sandialabs/staged-script/commit/d4823f42b4cf436bfbf67a3839236ae4e60859fc))

### Documentation
* docs: Remove WIP banner ([`59bd6ce`](https://github.com/sandialabs/staged-script/commit/59bd6ce2c0a44ef2572bb2ea1aff8dab8de39748))

  In preparation for the initial release, remove the banner indicating
  that open sourcing is still a work in progress.
* docs: Fix typo ([`e68b838`](https://github.com/sandialabs/staged-script/commit/e68b8381ff2afb250feabffd0c1569815da2ba62))
* docs: Create documentation and examples ([`5336421`](https://github.com/sandialabs/staged-script/commit/533642193d32bbb845f93378dbe30515fd47994e))
* docs: Stub out Sphinx documentation ([`00bd9af`](https://github.com/sandialabs/staged-script/commit/00bd9af22ac7691f085f9d546289b3506c7c77b7))
* docs: Add copyright/license text to source files ([`b0c22fc`](https://github.com/sandialabs/staged-script/commit/b0c22fcc011cb77ffada7d8614f63e435774818e))
* docs: Fix docstring issues ([`7365c87`](https://github.com/sandialabs/staged-script/commit/7365c87fdc5896677f64c6f906955da93c334fbb))
* docs: Update OpenSSF Best Practices badge ([`1633c78`](https://github.com/sandialabs/staged-script/commit/1633c7840c14dabebbecf8e4fa41260a4ad177e4))
* docs: Add contributing guidelines ([`8c04e16`](https://github.com/sandialabs/staged-script/commit/8c04e165356ff55f00575c8378fd6807ce75eef8))
* docs: Add code of conduct ([`579786e`](https://github.com/sandialabs/staged-script/commit/579786e60711059432821c09e30e1ea31363a69d))
* docs: Add security guidelines ([`c66c1dd`](https://github.com/sandialabs/staged-script/commit/c66c1ddda1bcdc81438f543101bbb10bbbf93ff3))
* docs: Add README ([`29c2ed3`](https://github.com/sandialabs/staged-script/commit/29c2ed396ce618bf5179d73973e29ed56dbf04a1))
* docs: Add license file ([`4be6ebf`](https://github.com/sandialabs/staged-script/commit/4be6ebf6281d44dc28f15e6b3d5348ee4d0f2931))
* docs: Update docstrings ([`aaccd8d`](https://github.com/sandialabs/staged-script/commit/aaccd8df14069f3ac651f89c9d2bdba42ce4a4af))

  Provide additional clarity in `DriverScript`'s documentation.
* docs: Update syntax ([`5bb662a`](https://github.com/sandialabs/staged-script/commit/5bb662ab286be95ef78c17d91d6cef77649ccb25))

  Update the instructions for overriding `print_script_execution_summary`
  to use the |= syntax for updating dictionaries.
* docs: Use "subclass" everywhere ([`c6fa97d`](https://github.com/sandialabs/staged-script/commit/c6fa97dd7d4b778e6734b5e8c749536d40dd34f4))

  Instead of inconsistently switching between "subclass" and "child class"
  in docstrings, use "subclass" everywhere for consistency's sake.
* docs: Add docstrings to `stage` inner functions ([`09b4797`](https://github.com/sandialabs/staged-script/commit/09b4797d7fa5f12668d7789d342dbcf64387d679))

  The number and size of the inner functions for the `stage` decorator are
  getting substantial enough that they really need docstrings at this
  point.
* docs: Update docstrings for stage methods ([`966103c`](https://github.com/sandialabs/staged-script/commit/966103c5d7263bc895de27474aaea401bfa22f06))

  Fill in all the details regarding subclassing that were omitted in
  earlier commits.

### Features
* feat!: Create RetryStage exception ([`d5e8941`](https://github.com/sandialabs/staged-script/commit/d5e8941232f86c0a4335974e7aaad5d2a47b61eb))

  Rather than relying on stages raising a `tenacity.TryAgain` exception to
  trigger retrying a stage, add a `RetryStage` exception to the package.
  This makes things more explicit for subclass developers, and makes it
  such that something outside the subclass developer's control that
  happens to raise a `TryAgain` doesn't trigger retying the stage, unless
  of course the subclass developer catches it and then raises a
  `RetryStage` in its place.

  Note that this is a breaking change, because any subclasses relying on
  raising `TryAgain` to trigger a stage retry will need to be updated to
  raise the new exception.
* feat: Add script name/stem attributes ([`74c387d`](https://github.com/sandialabs/staged-script/commit/74c387dba4bce011d8cc14129bcec2d47b3430e0))

  Capture the name and stem of the file being executed as attributes of
  `DriverScript` such that subclass developers can easily refer to them
  rather than determining them on the fly. This is useful for things like
  the script execution summary.

  Also add a unit test for `raise_parser_error()`, which was accidentally
  omitted in a prior commit.
* feat: Add help formatter to package ([`b458d95`](https://github.com/sandialabs/staged-script/commit/b458d959005422788646899a5cf70b91e04957ab))

  Add a class to the `driver_script` package to use as a formatter class
  for the `DriverScript` `ArgumentParser`. Make it such that the parser
  description is treated as raw text (no automatic formatting is done),
  and show the default values for all arguments.
* feat: Add flag for printing commands ([`7a7a0e0`](https://github.com/sandialabs/staged-script/commit/7a7a0e0cc386e35698da4d0c5433e4d18091e828))

  Add a flag when instantiating a `DriverScript` to govern whether
  commands should be printed immediately before running them. Default it
  to `True` for backwards compatibility. Also provide a keyword argument
  to the `run()` method that, if specified, will override the class flag.
  In this way users could, e.g., instantiate a `DriverScript`, telling it
  to print all commands, and then specify that certain commands should not
  be printed. The opposite of this is also possible (e.g., don't print
  any commands, except this one and that one).
* feat: Add raise_parser_error ([`0f60f8d`](https://github.com/sandialabs/staged-script/commit/0f60f8d9bc8c80e3529a8e7abb69b8e76da4e480))

  Add a method to the `DriverScript` base class to raise a parser error
  when a user has done something wrong in specifying the command line
  arguments. This differs from `argparse.ArgumentParser.error()` in that
  it's a little more user friendly, printing the help text first, and then
  the particular error in yellow.
* feat: Capture script success/failure ([`68ea1ae`](https://github.com/sandialabs/staged-script/commit/68ea1ae93532e58da8d96e0e3a36381d2551295b))

  Provide an instance attribute to allow subclass developers to toggle
  whether the script has succeeded or failed, and include the result in
  the script execution summary.
* feat!: Add stage retry functionality ([`d27ce6f`](https://github.com/sandialabs/staged-script/commit/d27ce6fed864fa7935d6f636c201b1733c85f34f))

  Add the ability to automatically retry a stage that raises a
  `tenacity.TryAgain` exception:

  * Provide default implementations for methods to prepare to retry a
    stage and appropriately handle when retrying ultimately fails, while
    allowing subclass developers to override them or customize them on a
    stage-by-stage basis.
  * Provide documentation to instruct subclass developers on how to make
    use of the retry functionality.
  * Wrap the **Begin-Stage Actions**, **Stage Body**, and **End-Stage
    Actions** in the retrying loop.

  Note that this is marked as a breaking change, as it's unclear what will
  happen to any subclasses that implemented their own stage retry
  functionality outside of this. The safest thing will be for subclass
  developers to update their subclasses to use this capability now
  provided by the base class.
* feat!: Provide retry args for every stage ([`281c376`](https://github.com/sandialabs/staged-script/commit/281c37644a02fec16efc0ea73de5c33549183ee4))

  Automatically add command line arguments to govern stage retry behavior
  (number of retry attempts, how long to wait between retries, total time
  to spend trying the stage) for every stage defined in a subclass.

  Note that this is a breaking change, because existing subclasses that
  currently define identical command line arguments will no longer work.
  Subclasses must be updated to remove their retry arguments and allow the
  base class to define them.
* feat: Allow custom "skip stage" phases ([`7b27bfa`](https://github.com/sandialabs/staged-script/commit/7b27bfa06fd4e2660063cf6618665a939402f911))

  Provide subclass developers with the flexibility to specialize the "skip
  stage" actions on a stage by stage basis.
* feat: Allow custom "end stage" phases ([`b30ea55`](https://github.com/sandialabs/staged-script/commit/b30ea5581ed1f9b8012c9e21f9506ee18b6a9661))

  Provide subclass developers with the flexibility to specialize the "end
  stage" actions on a stage by stage basis.
* feat: Add post-stage actions ([`8670752`](https://github.com/sandialabs/staged-script/commit/8670752aecf9dcb13264db677018cec6a57e2500))

  Add the flexibility to allow subclass designers to specify post-stage
  actions to run after a stage ends. These can be specified for all
  stages, and they can also optionally be customized on a stage by stage
  basis.
* feat: Allow custom "begin stage" phases ([`f05a5d4`](https://github.com/sandialabs/staged-script/commit/f05a5d47c03e86ad650307c02eefaa903f4d9e04))

  Provide subclass developers with the flexibility to specialize the
  "begin stage" actions on a stage by stage basis.
* feat: Add pre-stage actions ([`fb6d51e`](https://github.com/sandialabs/staged-script/commit/fb6d51e98797280e432423eb344f88c3d520100e))

  Add the flexibility to allow subclass designers to specify pre-stage
  actions to run before a stage begins. These can be specified for all
  stages, and they can also optionally be customized on a stage by stage
  basis.
* feat: Add script execution summary ([`689a84a`](https://github.com/sandialabs/staged-script/commit/689a84a6073cd7a74184c770a8decf894b967cc3))

  Add the ability to generate a summary of everything that was done by a
  derivative of `DriverScript`, including:

  * The effective command line invocation of the script.
  * Any commands executed in the underlying shell.
  * A timing report of the stages executed.
  * Any additional information the user wishes to pass in.
* feat!: Allow stages to be run multiple times ([`e147b03`](https://github.com/sandialabs/staged-script/commit/e147b03f837268fb2927f1c8a0b7c3957b7d9c0b))

  Convert the `durations` attribute from a `dict` to a `list` to allow for
  the possibility that one or more stages might be run multiple times
  (e.g., if something failed). Introduce a `StageDuration` class that
  inherits from `NamedTuple`, such that the entries added to the list must
  always be a `(str, timedelta)` `tuple` that will from then on be
  immutable and allow easy member access via dot notation.

### Refactoring
* refactor: Use functools.cached_property instead ([`3d91282`](https://github.com/sandialabs/staged-script/commit/3d91282518331e91c650f6c76815b2cf5b18e030))

  This package was originally developed for Python 3.6, before
  `functools.cached_property` was introduced. That should be a drop-in
  replacement for the home-grown `lazy_property`, though, so now that we
  just support Python 3.8+, we should use it instead.
* refactor: Support down to Python 3.8 ([`0c69f03`](https://github.com/sandialabs/staged-script/commit/0c69f0310d73837eb11d428c9e1807e3f4fd7eaf))

  * Switch type hinting to the older style.
  * Use `dict.update()` instead of the `|=` operator.
* refactor: Reduce setup file ([`b233553`](https://github.com/sandialabs/staged-script/commit/b23355399007e17f023750d33a46020b33b817fb))

  Remove the guts of the `setup.py` file so it just uses the
  `pyproject.toml` under the hood.
* refactor: Specify UTC timezone ([`1a95cd0`](https://github.com/sandialabs/staged-script/commit/1a95cd0050d6a2edb39287f185a360555436ff21))
* refactor: Explicitly don't check for errors ([`ed9d050`](https://github.com/sandialabs/staged-script/commit/ed9d050ed6bd374351bd43b740827d1a4eb5758e))
* refactor: Re-raise exception correctly ([`889645d`](https://github.com/sandialabs/staged-script/commit/889645d21b727484074c91adcf9303588763d711))
* refactor: Save exception messages to variable ([`2715390`](https://github.com/sandialabs/staged-script/commit/27153901503919e09065b45b32322119d3e6ca28))
* refactor!: Make boolean parameters keyword-only ([`2f3098f`](https://github.com/sandialabs/staged-script/commit/2f3098f8d20e3ab306bc98654d351f9608ad3193))
* refactor!: Rename package ([`8f42c66`](https://github.com/sandialabs/staged-script/commit/8f42c66c38e53c0d7a96029cfda40dc8b26fb798))

  Rename `driver-script` to `staged-script` in preparation for a future
  decoupling of the stage behavior from the shell interaction.
* refactor: Rearrange DriverScript class ([`e351982`](https://github.com/sandialabs/staged-script/commit/e3519823825041f0fe7a17f13aee3988098d0f89))

  Rearrange the methods in the `DriverScript` class to make the class
  easier to understand. No functional changes; just cut from here, paste
  to there. Also prefix some methods with `_` to indicate they're only
  intended for internal use.
* refactor!: Stages no longer registered by default ([`b3ac262`](https://github.com/sandialabs/staged-script/commit/b3ac2625abc12f88b5549926e1c1788e648a1c2c))

  Since its inception, `DriverScript`'s `stage` decorator has attempted
  to capture all the `stage`s defined by `DriverScript` subclasses in the
  `stages` class variable automatically. The desire was to keep things as
  easy as possible for subclass developers, in that all they'd need to do
  was inherit from `DriverScript`, define some methods decorated with
  `stage`, and then `DriverScript` would automatically handle things like
  stage-specific arguments (retries, etc.) and methods (pre/post,
  begin/end, etc.). Unfortunately this feature has been a thorn in our
  side for development, due to, e.g., `pytest` multiple-loading modules
  (and therefore redefining stages), `DriverScript` subclass hierarchies,
  etc.

  In order to pave the way for the flexibility for one `DriverScript`
  subclass to use stages defined within a separate `DriverScript`
  subclass, this commit makes it such that stages are no longer
  automatically registered. Instead subclass developers must pass the set
  of stages to register into the constructor when instantiating an object.
  This is a minor inconvenience, but it removes a good deal of hacky code
  and makes it such that `DriverScript` subclasses are decoupled from one
  another, so we believe the change is well worth it in the long run.

  Note that this is a breaking change, as all subclasses must be update
  their constructor definitions and any instantiations.
* refactor!: Switch stages to standard set ([`525fd79`](https://github.com/sandialabs/staged-script/commit/525fd792f39b70ae2cf6e6232fb270b70d6f9851))

  Initially the `stages` attribute of a `DriverScript` class was
  implemented as an ordered set (which in Python is a value-less `dict`
  converted to a `list`). The thinking there was that a `DriverScript`
  subclass should define a series of stages in order and they would be
  executed in that order. However, this failed to consider the following
  use case: Class `A` inherits from `DriverScript` and defines a few
  stages, then class `B` inherits from `A` and defines few more, but the
  intended sequence of stages isn't all from `A` followed by all from `B`;
  instead, they're meant to be interspersed. Since this is a valid use
  case, it makes sense to switch `stages` over to a standard `set`.

  Another motivation for the `stages` being an ordered set was considering
  the possibility of wanting to return to a prior stage if a certain stage
  failed. Consider an example `DriverScript` subclass with stages to
  configure, build, and test a code. If the test stage fails, perhaps the
  failure was seemingly random, and it'd be worthwhile to automatically
  rewind and retry the build and test stages again before notifying anyone
  of the failure. Or perhaps a certain regex match in the test output
  indicates you should rewind further and reconfigure. However, after
  further reflection, allowing such flexibility would open up a can of
  worms that probably shouldn't be opened. `DriverScript` already allows
  a subclass developer to automatically retry a stage. If something's
  happening that would cause you to back up further than the current stage
  and try things again, that probably means there's flakiness either in
  your code base or its surrounding infrastructure that a human should
  look into, so `DriverScript` probably shouldn't allow you to hide that.

  Note that this might be a breaking change if any subclasses were relying
  on the ordering of the `stages`.
* refactor: Use function from `reverse_argparse` ([`1c7fae0`](https://github.com/sandialabs/staged-script/commit/1c7fae05ff25a11e638f97e4cdc5827e001eccea))

  Since `reverse_argparse` now provides `quote_arg_if_necessary()` as a
  public function, use this instead of reimplementing the functionality in
  `DriverScript`.
* refactor!: Set current stage earlier ([`27d571f`](https://github.com/sandialabs/staged-script/commit/27d571f83f600ec7fdcb194ba010f5a8bfa3e1d5))

  Set the `current_stage` upon entering the `stage` wrapper, rather than
  in the `_begin_stage` method. Use `current_stage` in place of the
  `stage_name` passed into the wrapper, where appropriate.

  Note that this is a breaking change, as it changes the signature for the
  `_begin_stage` method.
* refactor: Get phase method rather than running it ([`8af3f75`](https://github.com/sandialabs/staged-script/commit/8af3f755db304b827fb358f60f848bed8fb07b01))

  In preparation for adding automatic retry functionality to the `stage`
  decorator, rewrite the `run_phase` method such that instead of running
  the method corresponding to the phase, it simply returns the `Callable`,
  which is then run outside the function. This generalization will make
  it such that we can pass a phase method to the `Retrying` object when
  we're ready for that.
* refactor: Wrap retryable phases into a function ([`345b77c`](https://github.com/sandialabs/staged-script/commit/345b77c0faf2fcdb98f4a90408b2981205b575f7))

  In preparation for adding automatic retry functionality to the stage
  decorator, wrap the phases that are to be retried into a function so
  they're easy to call together.
* refactor!: Stages always return None ([`b1238be`](https://github.com/sandialabs/staged-script/commit/b1238be88d25f0cb7225287544dbecda1c6b4a35))

  In preparation for adding stage retry functionality, make it such that a
  function decorated with `DriverScript.stage` must return `None`. This
  is reasonable because a conceptual stage of a script *does* something,
  but doesn't *return* something.

  Note that this is a breaking change for `DriverScript`, as any
  subclasses relying on returning values from functions decorated with
  `stage` will no longer work. A follow-up commit will fix this problem
  for `GMSSystemTest`.
* refactor: Change custom naming convention ([`e0b0f5f`](https://github.com/sandialabs/staged-script/commit/e0b0f5fef72f8ed36bbd7aab8f18b0b43e98d7bc))

  For simplicity's sake, when specializing one of the stage phases for a
  particular stage, just append the stage name to the end of the default
  method name.
* refactor: Consolidate helper functions ([`980dd7c`](https://github.com/sandialabs/staged-script/commit/980dd7c3f044c47de04ed62793a74798ca4bcbdc))

  Replace the helper functions inside the `stage` decorator with a single
  one that executes the correct methods based on input arguments.
* refactor: Use finally to end the stage ([`c8539ba`](https://github.com/sandialabs/staged-script/commit/c8539ba89ee2783e7eab3dcb39360f6fea5409fe))

  Rather than having `_end_stage()` called in two different places,
  consolidate those calls into one using a `finally` clause of the `try`
  block.
* refactor: Add `run` method ([`2fe663a`](https://github.com/sandialabs/staged-script/commit/2fe663a083ebb906e0f72006ae8c0de6b7db99c7))

  Create a `run` method to wrap calls to `subprocess.run` and capture the
  command executed.
* refactor: Add `parse_args` method to base class ([`c73e8eb`](https://github.com/sandialabs/staged-script/commit/c73e8eb5cb546d2dd48385c32259da22e991df25))

  Add the `parse_args` method to the `DriverScript` base class to handle
  parsing the command line argument supplied by the base class. This will
  be overridden and extended by child classes.
* refactor: Add parser property to base class ([`1c4f10f`](https://github.com/sandialabs/staged-script/commit/1c4f10fae8ca5843c026c8fc8ef3103db1c094d4))

  Add a `parser` lazily-evaluated property to the `DriverScript` base
  class to handle parsing of arguments supplied by the base class. This
  will be overridden and extended by child classes.
* refactor: Use Rich Table for timing report ([`1d24cd1`](https://github.com/sandialabs/staged-script/commit/1d24cd1d6c17602925ced11dc87900046f1ca3d5))

  Rather than generating the timing report table manually, use
  `rich.table.Table` to handle the magic automatically. Also abandon the
  Markdown format for the table, as Rich's default styling looks nicer,
  and if a user needs to copy it into an issue, they can always place it
  in a code block.
* refactor: Create DriverScript base class ([`bb8ea46`](https://github.com/sandialabs/staged-script/commit/bb8ea46040a3e8b0939a712b036f373e6bd7b9c6))

  Create an initial cut of the `DriverScript` base class, such that any
  Python scripts designed to drive a series of commands in the underlying
  shell can inherit from it.

### Testing
* test: Cover `run()` in dry-run mode ([`c44d6ff`](https://github.com/sandialabs/staged-script/commit/c44d6ffb2b7965c0b4ee460b167c0af2b51a20fa))
* test: Add coverage configuration ([`27bc6d6`](https://github.com/sandialabs/staged-script/commit/27bc6d62408a42b4b99b5d5634890595454d3d0b))
* test: Fix imports for unit/integration tests ([`e1836e3`](https://github.com/sandialabs/staged-script/commit/e1836e31a7c56d33d77b8c1736d147d279105e17))
* test: Rename tests ([`2723351`](https://github.com/sandialabs/staged-script/commit/27233514efb2797f8f8fe8e561d9377bbb9677e3))

  The convention is to name tests `test_<function_to_test>`, but these
  tests accidentally omitted the leading underscore.
* test: Rename test fixtures ([`5f7b063`](https://github.com/sandialabs/staged-script/commit/5f7b06329b07dfdc8a773889bf5c9ee8c910ac59))

  Remove acronyms for clarity.
* test: Disable warning on too many parametrizations ([`99e59d9`](https://github.com/sandialabs/staged-script/commit/99e59d9fa80f2c0764583b04556ff4655e399d1a))
* test: Remove duplicate test case ([`176bb6f`](https://github.com/sandialabs/staged-script/commit/176bb6f241564d8833658052966f7d560edcf133))
* test: Reduce cognitive complexity ([`5153a1b`](https://github.com/sandialabs/staged-script/commit/5153a1bd53fad090346c989ede9be536056f3824))

  Extract a method from the test to reduce the amount of
  copy/paste/modify.
* test: Complete testing of `DriverScript` ([`298b4a9`](https://github.com/sandialabs/staged-script/commit/298b4a9bc35a5281ceab27fc300ed6dc1a8d8f0f))

  Create a basic subclass of `DriverScript` to test the functionality of
  the `stage` decorator.
* test!: Cover `_add_stage` ([`e079a72`](https://github.com/sandialabs/staged-script/commit/e079a729ef38bf123b0b94ba1836ded048b1fd3c))

  Ensure `_add_stage` results in the correct list of `stages`, and that
  invalid identifiers do indeed throw an exception.

  Note that this is a breaking change because it now disallows certain
  stage names that were previously allowable.
* test: Cover additional case ([`0ede83f`](https://github.com/sandialabs/staged-script/commit/0ede83f6b70d719c4875a67946c1a05e924d9566))

  Cover the base case when no additional sections are supplied when
  printing the script execution summary.
