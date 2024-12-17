# CHANGELOG



## v2.0.1 (2024-12-17)

### Chores
* chore(deps): Bump the github-actions-dependencies group with 2 updates ([`87d42a8`](https://github.com/sandialabs/staged-script/commit/87d42a8c38546ac3be8b3240b81c5ac4f867d6f8))

  Bumps the github-actions-dependencies group with 2 updates: [github/codeql-action](https://github.com/github/codeql-action) and [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).


  Updates `github/codeql-action` from 3.27.6 to 3.27.9
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/aa578102511db1f4524ed59b8cc2bae4f6e88195...df409f7d9260372bd5f19e5b04e83cb3c43714ae)

  Updates `python-semantic-release/python-semantic-release` from 9.15.1 to 9.15.2
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/a3233795eb26b6d5167192ffd4550947d764a9b0...7b3f71697ccfbaef884e1e754b6364e974b134cf)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 4 updates ([`7b50ecb`](https://github.com/sandialabs/staged-script/commit/7b50ecbf31b161455c845d79557535fafc641d7e))

  Bumps the github-actions-dependencies group with 4 updates: [github/codeql-action](https://github.com/github/codeql-action), [codecov/codecov-action](https://github.com/codecov/codecov-action), [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) and [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish).


  Updates `github/codeql-action` from 3.27.5 to 3.27.6
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/f09c1c0a94de965c15400f5634aa42fac8fb8f88...aa578102511db1f4524ed59b8cc2bae4f6e88195)

  Updates `codecov/codecov-action` from 5.0.7 to 5.1.1
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/015f24e6818733317a2da2edd6290ab26238649a...7f8b4b4bde536c465e797be725718b88c5d95e0e)

  Updates `python-semantic-release/python-semantic-release` from 9.15.0 to 9.15.1
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/2773f6d901a5cefed959c6ccda302ef41fed67dc...a3233795eb26b6d5167192ffd4550947d764a9b0)

  Updates `pypa/gh-action-pypi-publish` from 1.12.2 to 1.12.3
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/15c56dba361d8335944d31a2ecd17d700fc7bcbc...67339c736fd9354cd4f8cb0b744f2b82a74b5c70)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>

### Patch
* patch: Support Python 3.13 ([`c0a242c`](https://github.com/sandialabs/staged-script/commit/c0a242c8c3a1866aff0c923c0088a602b51b8350))

## v2.0.0 (2024-12-03)

### Chores
* chore!: Drop support for Python 3.8 ([`a9c8005`](https://github.com/sandialabs/staged-script/commit/a9c80052734c44f8d25bbce7599b315ac627c639))

  * Use type-hinting provided out of the box in 3.9.
  * Use new dictionary update syntax.
  * Update the docs and CI accordingly.
* chore(deps): Bump python-semantic-release/python-semantic-release ([`ff58fa2`](https://github.com/sandialabs/staged-script/commit/ff58fa2de2e4274b6741c039b4b151d5d46dcc22))

  Bumps the github-actions-dependencies group with 1 update: [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).


  Updates `python-semantic-release/python-semantic-release` from 9.14.0 to 9.15.0
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/825655a47c9f7496f99ab144d28c424d40333a8a...2773f6d901a5cefed959c6ccda302ef41fed67dc)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 4 updates ([`a8c46c2`](https://github.com/sandialabs/staged-script/commit/a8c46c21a011735efe5e4fbae564b3a8f7f7173f))

  Bumps the github-actions-dependencies group with 4 updates: [step-security/harden-runner](https://github.com/step-security/harden-runner), [github/codeql-action](https://github.com/github/codeql-action), [codecov/codecov-action](https://github.com/codecov/codecov-action) and [actions/dependency-review-action](https://github.com/actions/dependency-review-action).


  Updates `step-security/harden-runner` from 2.10.1 to 2.10.2
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/91182cccc01eb5e619899d80e4e971d6181294a7...0080882f6c36860b6ba35c610c98ce87d4e2f26f)

  Updates `github/codeql-action` from 3.27.4 to 3.27.5
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/ea9e4e37992a54ee68a9622e985e60c8e8f12d9f...f09c1c0a94de965c15400f5634aa42fac8fb8f88)

  Updates `codecov/codecov-action` from 5.0.2 to 5.0.7
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/5c47607acb93fed5485fdbf7232e8a31425f672a...015f24e6818733317a2da2edd6290ab26238649a)

  Updates `actions/dependency-review-action` from 4.4.0 to 4.5.0
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/4081bf99e2866ebe428fc0477b69eb4fcda7220a...3b139cfc5fae8b618d3eae3675e383bb1769c019)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 2 updates ([`0edf7d9`](https://github.com/sandialabs/staged-script/commit/0edf7d92b2fd7bfc1098dd7e0a5034fefd29371c))

  Bumps the github-actions-dependencies group with 2 updates: [github/codeql-action](https://github.com/github/codeql-action) and [codecov/codecov-action](https://github.com/codecov/codecov-action).


  Updates `github/codeql-action` from 3.27.1 to 3.27.4
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/4f3212b61783c3c68e8309a0f18a699764811cda...ea9e4e37992a54ee68a9622e985e60c8e8f12d9f)

  Updates `codecov/codecov-action` from 4.6.0 to 5.0.2
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/b9fd7d16f6d7d1b5d2bec1a2887e65ceed900238...5c47607acb93fed5485fdbf7232e8a31425f672a)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-major
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump the github-actions-dependencies group with 3 updates ([`d1dc93a`](https://github.com/sandialabs/staged-script/commit/d1dc93a89c629545b584bde28cbbf4a5e252c7ea))

  Bumps the github-actions-dependencies group with 3 updates: [github/codeql-action](https://github.com/github/codeql-action), [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) and [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish).


  Updates `github/codeql-action` from 3.27.0 to 3.27.1
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/662472033e021d55d94146f66f6058822b0b39fd...4f3212b61783c3c68e8309a0f18a699764811cda)

  Updates `python-semantic-release/python-semantic-release` from 9.12.0 to 9.14.0
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/c1bcfdbb994243ac7cf419365d5894d6bfb2950e...825655a47c9f7496f99ab144d28c424d40333a8a)

  Updates `pypa/gh-action-pypi-publish` from 1.11.0 to 1.12.2
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/fb13cb306901256ace3dab689990e13a5550ffaa...15c56dba361d8335944d31a2ecd17d700fc7bcbc)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
    dependency-group: github-actions-dependencies
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-minor
    dependency-group: github-actions-dependencies
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore: Group dependabot updates ([`aef5ea5`](https://github.com/sandialabs/staged-script/commit/aef5ea52cb2145382554b5c2bc600f1e261bcb7c))

  Run dependabot updates weekly instead of daily, and group them together
  for the different providers (GitHub Actions and pip), to reduce the
  amount of noise in the repository history.
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.3 to 1.11.0 ([`fe42697`](https://github.com/sandialabs/staged-script/commit/fe426972b3218994e7016903a4cc5f1186a7f2db))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.3 to 1.11.0.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/f7600683efdcb7656dec5b29656edb7bc586e597...fb13cb306901256ace3dab689990e13a5550ffaa)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/dependency-review-action from 4.3.5 to 4.4.0 ([`cab66b4`](https://github.com/sandialabs/staged-script/commit/cab66b4307b64efca876629882959b56b70d43c2))

  Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 4.3.5 to 4.4.0.
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/a6993e2c61fd5dc440b409aa1d6904921c5e1894...4081bf99e2866ebe428fc0477b69eb4fcda7220a)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 5.2.0 to 5.3.0 ([`4167ef5`](https://github.com/sandialabs/staged-script/commit/4167ef5644ba61b5458d11c6b0d4b1e82843411f))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5.2.0 to 5.3.0.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/f677139bbe7f9c59b41e40162b753c062f5d49a3...0b93645e9fea7318ecaed2b359559ac225c90a2b)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 4.2.1 to 4.2.2 ([`375e27b`](https://github.com/sandialabs/staged-script/commit/375e27bf6210136052640869cd05872a475ac801))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 4.2.1 to 4.2.2.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871...11bd71901bbe5b1630ceea73d27597364c9af683)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.13 to 3.27.0 ([`a2e592d`](https://github.com/sandialabs/staged-script/commit/a2e592dcdf37b1b2b321e2bc6f8b50cd766ba9bf))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.13 to 3.27.0.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/f779452ac5af1c261dce0346a8f964149f49322b...662472033e021d55d94146f66f6058822b0b39fd)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/dependency-review-action from 4.3.4 to 4.3.5 ([`e77a1ca`](https://github.com/sandialabs/staged-script/commit/e77a1ca1c42e7dedb92c5ca748110d07c69a6e03))

  Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 4.3.4 to 4.3.5.
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/5a2ce3f5b92ee19cbb1541a4984c76d921601d7c...a6993e2c61fd5dc440b409aa1d6904921c5e1894)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
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
* chore(deps): Bump python-semantic-release/python-semantic-release ([`706b2f1`](https://github.com/sandialabs/staged-script/commit/706b2f17d5bbd22656ceee33e0974480632f07c0))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.11.1 to 9.12.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/657118d28ae4a74d8a387bedf5db2bb7bac0cb33...c1bcfdbb994243ac7cf419365d5894d6bfb2950e)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump taskmedia/action-conventional-commits ([`070d086`](https://github.com/sandialabs/staged-script/commit/070d086bb05fe3736bf86e81ba6df21d1b3c6864))

  Bumps [taskmedia/action-conventional-commits](https://github.com/taskmedia/action-conventional-commits) from 1.1.18 to 1.1.19.
  - [Release notes](https://github.com/taskmedia/action-conventional-commits/releases)
  - [Changelog](https://github.com/taskmedia/action-conventional-commits/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/taskmedia/action-conventional-commits/compare/180c46eb0f4380691dc9845e68b1ef36c05d57d7...cb0de258e7309e163ee353a8c38e24e609608cd6)

  ---
  updated-dependencies:
  - dependency-name: taskmedia/action-conventional-commits
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`2a71321`](https://github.com/sandialabs/staged-script/commit/2a713213eb86a587c326775d63f50e9e2d15a933))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.10.1 to 9.11.1.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/d6ea6b856fc884559d9f66b4d9a7dd643fc82c6a...657118d28ae4a74d8a387bedf5db2bb7bac0cb33)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.12 to 3.26.13 ([`d6a7bbb`](https://github.com/sandialabs/staged-script/commit/d6a7bbbc897a5c81a3d032ead4a7f2e7e8a3447e))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.12 to 3.26.13.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/c36620d31ac7c881962c3d9dd939c40ec9434f2b...f779452ac5af1c261dce0346a8f964149f49322b)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`796bd6c`](https://github.com/sandialabs/staged-script/commit/796bd6cc18f042cc22128c9f9a01936a497fe386))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.10.0 to 9.10.1.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/18399a7209118c6f0bcc923857ef7052cc5de5e3...d6ea6b856fc884559d9f66b4d9a7dd643fc82c6a)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.4.1 to 4.4.3 ([`3fbbd14`](https://github.com/sandialabs/staged-script/commit/3fbbd14159ea0022a2bb74a4496f98116fb9d5b4))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.4.1 to 4.4.3.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/604373da6381bf24206979c74d06a550515601b9...b4b15b8c7c6ac21ea08fcf65892d2ee8f75cf882)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`11c9b1a`](https://github.com/sandialabs/staged-script/commit/11c9b1ad17ab96bcfdf715a40db016084eee69fc))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 76f1ffae08640b2714f1c333ef38895153e37f34 to 18399a7209118c6f0bcc923857ef7052cc5de5e3.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/76f1ffae08640b2714f1c333ef38895153e37f34...18399a7209118c6f0bcc923857ef7052cc5de5e3)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.11 to 3.26.12 ([`7dadc0e`](https://github.com/sandialabs/staged-script/commit/7dadc0e4d0d89551bf60cf5df32d0aa29960225e))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.11 to 3.26.12.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/6db8d6351fd0be61f9ed8ebd12ccd35dcec51fea...c36620d31ac7c881962c3d9dd939c40ec9434f2b)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.4.0 to 4.4.1 ([`484ec7f`](https://github.com/sandialabs/staged-script/commit/484ec7fbbe948f53d108c2bb39be929d635a2fcd))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.4.0 to 4.4.1.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/50769540e7f4bd5e21e526ee35c689e35e0d6874...604373da6381bf24206979c74d06a550515601b9)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 4.2.0 to 4.2.1 ([`2fe9e07`](https://github.com/sandialabs/staged-script/commit/2fe9e073774b6040f5bc2ec9c56fcba066d924df))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 4.2.0 to 4.2.1.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/d632683dd7b4114ad314bca15554477dd762a938...eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`8d355dc`](https://github.com/sandialabs/staged-script/commit/8d355dca803a49d03793158084f42cf1902c2553))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.9.0 to 9.10.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/fd8c509df1f16daf3f71a9a6fac49247017017b2...76f1ffae08640b2714f1c333ef38895153e37f34)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.2 to 1.10.3 ([`425f0e7`](https://github.com/sandialabs/staged-script/commit/425f0e7acde489ab3d6c0a8e51ac396f45b604eb))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.2 to 1.10.3.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/897895f1e160c830e369f9779632ebc134688e1b...f7600683efdcb7656dec5b29656edb7bc586e597)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.10 to 3.26.11 ([`90a8bcf`](https://github.com/sandialabs/staged-script/commit/90a8bcfb280ff89e1696197ee91eb6491b020fb9))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.10 to 3.26.11.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/e2b3eafc8d227b0241d48be5f425d47c2d750a13...6db8d6351fd0be61f9ed8ebd12ccd35dcec51fea)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump codecov/codecov-action from 4.5.0 to 4.6.0 ([`e566c12`](https://github.com/sandialabs/staged-script/commit/e566c12ea26f939b6d1da4e036564688e5f3eb63))

  Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 4.5.0 to 4.6.0.
  - [Release notes](https://github.com/codecov/codecov-action/releases)
  - [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/codecov/codecov-action/compare/e28ff129e5465c2c0dcc6f003fc735cb6ae0c673...b9fd7d16f6d7d1b5d2bec1a2887e65ceed900238)

  ---
  updated-dependencies:
  - dependency-name: codecov/codecov-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`aae46ad`](https://github.com/sandialabs/staged-script/commit/aae46adf4e34738a52cf40fba9a67518f887040f))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.8 to 9.8.9.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/fa2bbbf8e61069551abd513fdc5627e14c8637c7...0a92b5d7ebfc15a84f9801ebd1bf706343d43711)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.9 to 3.26.10 ([`ae2c4c5`](https://github.com/sandialabs/staged-script/commit/ae2c4c54750e8821656bd31fdcbf5728dde66036))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.9 to 3.26.10.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/461ef6c76dfe95d5c364de2f431ddbd31a417628...e2b3eafc8d227b0241d48be5f425d47c2d750a13)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`871df5d`](https://github.com/sandialabs/staged-script/commit/871df5d94558b583d2fa63934309ba140ae6b04c))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.9 to 9.9.0.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/cbe8eaaa7a06ef218fce69bd1bc01dd16483dc6d...fd8c509df1f16daf3f71a9a6fac49247017017b2)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`a2415f8`](https://github.com/sandialabs/staged-script/commit/a2415f8e0144eccf0e99bb25e274616b8fc271bb))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.8 to 9.8.9.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/fe6b271e942115b528c85e42bc19611b01dcea59...cbe8eaaa7a06ef218fce69bd1bc01dd16483dc6d)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 4.1.7 to 4.2.0 ([`cf393c6`](https://github.com/sandialabs/staged-script/commit/cf393c654b332c1a1e2dc0669ecee37a4c87d443))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 4.1.7 to 4.2.0.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/692973e3d937129bcbf40652eb9f2f61becf3332...d632683dd7b4114ad314bca15554477dd762a938)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.8 to 3.26.9 ([`1d1eace`](https://github.com/sandialabs/staged-script/commit/1d1eacee258cdcba6376a0025c427349f5c0aa21))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.8 to 3.26.9.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/294a9d92911152fe08befb9ec03e240add280cb3...461ef6c76dfe95d5c364de2f431ddbd31a417628)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.1 to 1.10.2 ([`e4965a4`](https://github.com/sandialabs/staged-script/commit/e4965a499b9a8c02a0fbbd84fc2cd6a1a09f79d9))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.1 to 1.10.2.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/0ab0b79471669eb3a4d647e625009c62f9f3b241...897895f1e160c830e369f9779632ebc134688e1b)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.7 to 3.26.8 ([`9f85785`](https://github.com/sandialabs/staged-script/commit/9f85785220c1540c8e2ba9e36cc30b1e8e44a6ee))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.7 to 3.26.8.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/8214744c546c1e5c8f03dde8fab3a7353211988d...294a9d92911152fe08befb9ec03e240add280cb3)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump taskmedia/action-conventional-commits ([`10d9899`](https://github.com/sandialabs/staged-script/commit/10d9899d1ba6f8bdad4f785cc64dd20fb97db267))

  Bumps [taskmedia/action-conventional-commits](https://github.com/taskmedia/action-conventional-commits) from 1.1.17 to 1.1.18.
  - [Release notes](https://github.com/taskmedia/action-conventional-commits/releases)
  - [Changelog](https://github.com/taskmedia/action-conventional-commits/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/taskmedia/action-conventional-commits/compare/866c0e6dba6aaaef9ad0939a40620b27888906c2...180c46eb0f4380691dc9845e68b1ef36c05d57d7)

  ---
  updated-dependencies:
  - dependency-name: taskmedia/action-conventional-commits
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.6 to 3.26.7 ([`94ea654`](https://github.com/sandialabs/staged-script/commit/94ea654f3f60286302cbb4d90c1a09026ecb4c9b))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.6 to 3.26.7.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/4dd16135b69a43b6c8efb853346f8437d92d3c93...8214744c546c1e5c8f03dde8fab3a7353211988d)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.9.1 to 2.10.1 ([`ef54321`](https://github.com/sandialabs/staged-script/commit/ef543210871a170626ab0b813c884aa97f6e1263))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.9.1 to 2.10.1.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/5c7944e73c4c2a096b17a9cb74d65b6c2bbafbde...91182cccc01eb5e619899d80e4e971d6181294a7)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`1bf4a4b`](https://github.com/sandialabs/staged-script/commit/1bf4a4bb9362ff262ad4b9f15d1104c2587d7794))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.7 to 9.8.8.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/17c75b706f81263690a0a0dc88d83415f783fc04...fa2bbbf8e61069551abd513fdc5627e14c8637c7)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.10.0 to 1.10.1 ([`8250f1a`](https://github.com/sandialabs/staged-script/commit/8250f1a2f1aa35f1cce4d69ce77c13ef4ce035d9))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.10.0 to 1.10.1.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/8a08d616893759ef8e1aa1f2785787c0b97e20d6...0ab0b79471669eb3a4d647e625009c62f9f3b241)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.0 ([`9af287f`](https://github.com/sandialabs/staged-script/commit/9af287f2b3c4453bcc8a1a749a99da99f8a9a741))

  Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.9.0 to 1.10.0.
  - [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
  - [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/ec4db0b4ddc65acdf4bff5fa45ac92d78b56bdf0...8a08d616893759ef8e1aa1f2785787c0b97e20d6)

  ---
  updated-dependencies:
  - dependency-name: pypa/gh-action-pypi-publish
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`ab3795a`](https://github.com/sandialabs/staged-script/commit/ab3795a83bc3134381bb72e00fb573b41ab4af1b))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.7 to 9.8.8.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/708671d0eb33bcbea78c5a3d81ae04c60deeddf3...fe6b271e942115b528c85e42bc19611b01dcea59)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.6 to 4.4.0 ([`4e7849f`](https://github.com/sandialabs/staged-script/commit/4e7849f056e0eb51e717cce05d6dc3c49fa7393f))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.6 to 4.4.0.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/834a144ee995460fba8ed112a2fc961b36a5ec5a...50769540e7f4bd5e21e526ee35c689e35e0d6874)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 5.1.1 to 5.2.0 ([`501a129`](https://github.com/sandialabs/staged-script/commit/501a12924e24b6aab881c38107d13df057ac6242))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5.1.1 to 5.2.0.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/39cd14951b08e74b54015e9e001cdefcf80e669f...f677139bbe7f9c59b41e40162b753c062f5d49a3)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.5 to 3.26.6 ([`906f129`](https://github.com/sandialabs/staged-script/commit/906f129bd830cbdab955553559ff1c286537851e))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.5 to 3.26.6.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/2c779ab0d087cd7fe7b826087247c2c81f27bfa6...4dd16135b69a43b6c8efb853346f8437d92d3c93)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.4 to 3.26.5 ([`8a6e793`](https://github.com/sandialabs/staged-script/commit/8a6e793d4b5fa026514deb43222abd3aafcb0344))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.4 to 3.26.5.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/f0f3afee809481da311ca3a6ff1ff51d81dbeb24...2c779ab0d087cd7fe7b826087247c2c81f27bfa6)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.3 to 3.26.4 ([`4b1f28b`](https://github.com/sandialabs/staged-script/commit/4b1f28b1b6973d8e9a2e8d6fa1132b0a5b05ef4b))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.3 to 3.26.4.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/883d8588e56d1753a8a58c1c86e88976f0c23449...f0f3afee809481da311ca3a6ff1ff51d81dbeb24)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`2737b8c`](https://github.com/sandialabs/staged-script/commit/2737b8cb204d0ac09432734902122cd5bba6ebbb))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.6 to 9.8.7.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/dec06aa649fddae6610bc64878868498bfcbad7b...708671d0eb33bcbea78c5a3d81ae04c60deeddf3)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`328c843`](https://github.com/sandialabs/staged-script/commit/328c843502c7d8cfc36ece5ff19d151f2942b0cd))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.6 to 9.8.7.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/0dcddac3ba7b691d7a3fd4586b640d7b214a0016...17c75b706f81263690a0a0dc88d83415f783fc04)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.2 to 3.26.3 ([`b65558c`](https://github.com/sandialabs/staged-script/commit/b65558cd64013d0949d107512e64b1ed1889652b))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.2 to 3.26.3.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/429e1977040da7a23b6822b13c129cd1ba93dbb2...883d8588e56d1753a8a58c1c86e88976f0c23449)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.1 to 3.26.2 ([`09820ab`](https://github.com/sandialabs/staged-script/commit/09820ab3e88353da0801ec5ba2d7831fd9e305bf))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.1 to 3.26.2.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/29d86d22a34ea372b1bbf3b2dced2e25ca6b3384...429e1977040da7a23b6822b13c129cd1ba93dbb2)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.26.0 to 3.26.1 ([`788c951`](https://github.com/sandialabs/staged-script/commit/788c951131332884e229dacdc048d7847f9f1ce8))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.26.0 to 3.26.1.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/eb055d739abdc2e8de2e5f4ba1a8b246daa779aa...29d86d22a34ea372b1bbf3b2dced2e25ca6b3384)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.15 to 3.26.0 ([`cf27cc1`](https://github.com/sandialabs/staged-script/commit/cf27cc1a9e155df1e3f35e377311bd468170ced6))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.15 to 3.26.0.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/afb54ba388a7dca6ecae48f608c4ff05ff4cc77a...eb055d739abdc2e8de2e5f4ba1a8b246daa779aa)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.9.0 to 2.9.1 ([`73cea5d`](https://github.com/sandialabs/staged-script/commit/73cea5dee94636e8d6d088c82278470eb78793ba))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.9.0 to 2.9.1.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/0d381219ddf674d61a7572ddd19d7941e271515c...5c7944e73c4c2a096b17a9cb74d65b6c2bbafbde)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.5 to 4.3.6 ([`914ba07`](https://github.com/sandialabs/staged-script/commit/914ba070d18667f07f8964d28958e4e4c20eb807))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.5 to 4.3.6.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/89ef406dd8d7e03cfd12d9e0a4a378f454709029...834a144ee995460fba8ed112a2fc961b36a5ec5a)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.4 to 4.3.5 ([`4ebe4ef`](https://github.com/sandialabs/staged-script/commit/4ebe4ef9a3136aa705413eba34b73434caf08686))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.4 to 4.3.5.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/0b2256b8c012f0828dc542b3febcab082c67f72b...89ef406dd8d7e03cfd12d9e0a4a378f454709029)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump ossf/scorecard-action from 2.3.3 to 2.4.0 ([`e957819`](https://github.com/sandialabs/staged-script/commit/e957819da60d77b22794029d1ccb9699f83683b7))

  Bumps [ossf/scorecard-action](https://github.com/ossf/scorecard-action) from 2.3.3 to 2.4.0.
  - [Release notes](https://github.com/ossf/scorecard-action/releases)
  - [Changelog](https://github.com/ossf/scorecard-action/blob/main/RELEASE.md)
  - [Commits](https://github.com/ossf/scorecard-action/compare/dc50aa9510b46c811795eb24b2f1ba02a914e534...62b2cac7ed8198b15735ed49ab1e5cf35480ba46)

  ---
  updated-dependencies:
  - dependency-name: ossf/scorecard-action
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.14 to 3.25.15 ([`b12cd9c`](https://github.com/sandialabs/staged-script/commit/b12cd9c84adfd66ffa7d8670c3a928930237e1eb))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.14 to 3.25.15.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/5cf07d8b700b67e235fbb65cbc84f69c0cf10464...afb54ba388a7dca6ecae48f608c4ff05ff4cc77a)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.13 to 3.25.14 ([`885edba`](https://github.com/sandialabs/staged-script/commit/885edbae3d340c9debc6a901f76acc2cc38d83ee))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.13 to 3.25.14.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/2d790406f505036ef40ecba973cc774a50395aac...5cf07d8b700b67e235fbb65cbc84f69c0cf10464)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`973dcb7`](https://github.com/sandialabs/staged-script/commit/973dcb7bb9ddab70ab7c0a1ed8a7d9cbeeb019a9))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.5 to 9.8.6.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/fe6cc89b43d8cbf0f9ce3285df3f77ff69c9b5d4...0dcddac3ba7b691d7a3fd4586b640d7b214a0016)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`54959e2`](https://github.com/sandialabs/staged-script/commit/54959e28f4fa80fff2d6d700b31e19badae78d1e))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.5 to 9.8.6.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/3ba53469e72452e7597dd5c61851e6fbf294420b...dec06aa649fddae6610bc64878868498bfcbad7b)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.12 to 3.25.13 ([`994768d`](https://github.com/sandialabs/staged-script/commit/994768dba83d6af3438485978cfea35381147253))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.12 to 3.25.13.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/4fa2a7953630fd2f3fb380f21be14ede0169dd4f...2d790406f505036ef40ecba973cc774a50395aac)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump step-security/harden-runner from 2.8.1 to 2.9.0 ([`82d0473`](https://github.com/sandialabs/staged-script/commit/82d047311adef7e39ad29e237ebb1a44beb4e8d9))

  Bumps [step-security/harden-runner](https://github.com/step-security/harden-runner) from 2.8.1 to 2.9.0.
  - [Release notes](https://github.com/step-security/harden-runner/releases)
  - [Commits](https://github.com/step-security/harden-runner/compare/17d0e2bd7d51742c71671bd19fa12bdc9d40a3d6...0d381219ddf674d61a7572ddd19d7941e271515c)

  ---
  updated-dependencies:
  - dependency-name: step-security/harden-runner
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/dependency-review-action from 4.3.3 to 4.3.4 ([`9cb6064`](https://github.com/sandialabs/staged-script/commit/9cb6064ffe9ea96712e99a1a7715604ba8fdd1d7))

  Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 4.3.3 to 4.3.4.
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/72eb03d02c7872a771aacd928f3123ac62ad6d3a...5a2ce3f5b92ee19cbb1541a4984c76d921601d7c)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 3.25.11 to 3.25.12 ([`bcd2a8e`](https://github.com/sandialabs/staged-script/commit/bcd2a8e2718e51db0a8132ae500c6f513670d728))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 3.25.11 to 3.25.12.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/b611370bb5703a7efb587f9d136a52ea24c5c38c...4fa2a7953630fd2f3fb380f21be14ede0169dd4f)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 5.1.0 to 5.1.1 ([`c6e3d88`](https://github.com/sandialabs/staged-script/commit/c6e3d8810a567d8a23a4df65b5f52a383ae1b4df))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 5.1.0 to 5.1.1.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/82c7e631bb3cdc910f68e0081d67478d79c6982d...39cd14951b08e74b54015e9e001cdefcf80e669f)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`541b776`](https://github.com/sandialabs/staged-script/commit/541b77653c498a09e4475982fa063c3ca3574fae))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.4 to 9.8.5.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/ab38ab601e1cc0a20e26d1ab089e0b9d40d7faf0...fe6cc89b43d8cbf0f9ce3285df3f77ff69c9b5d4)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`7975973`](https://github.com/sandialabs/staged-script/commit/7975973f3c4f5221c61a7b57e322944f100dd4ca))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.4 to 9.8.5.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/e02a9bdd3adb36d18390120c123ce6b7b3bae359...3ba53469e72452e7597dd5c61851e6fbf294420b)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/upload-to-gh-release ([`2641707`](https://github.com/sandialabs/staged-script/commit/26417075b4517bc7eb966ce7cef3d82f0c5076e1))

  Bumps [python-semantic-release/upload-to-gh-release](https://github.com/python-semantic-release/upload-to-gh-release) from 9.8.3 to 9.8.4.
  - [Release notes](https://github.com/python-semantic-release/upload-to-gh-release/releases)
  - [Changelog](https://github.com/python-semantic-release/upload-to-gh-release/blob/main/releaserc.toml)
  - [Commits](https://github.com/python-semantic-release/upload-to-gh-release/compare/c7c3b69570cbd3011111d2673d8f07142473a871...ab38ab601e1cc0a20e26d1ab089e0b9d40d7faf0)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/upload-to-gh-release
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/upload-artifact from 4.3.3 to 4.3.4 ([`5233703`](https://github.com/sandialabs/staged-script/commit/52337035dac9041bee4d97861af3aeb5ad4f59bb))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 4.3.3 to 4.3.4.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/65462800fd760344b1a7b4382951275a0abb4808...0b2256b8c012f0828dc542b3febcab082c67f72b)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump python-semantic-release/python-semantic-release ([`6c60341`](https://github.com/sandialabs/staged-script/commit/6c603412124803daa824f4ccdf9547d872a5cb74))

  Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from adc0c15810c0b9ee22c43d85d1890b394d49a641 to e02a9bdd3adb36d18390120c123ce6b7b3bae359.
  - [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
  - [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/adc0c15810c0b9ee22c43d85d1890b394d49a641...e02a9bdd3adb36d18390120c123ce6b7b3bae359)

  ---
  updated-dependencies:
  - dependency-name: python-semantic-release/python-semantic-release
    dependency-type: direct:production
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore: Update LICENSE/COPYRIGHT files ([`bcf3433`](https://github.com/sandialabs/staged-script/commit/bcf34339f29b1da38553d3477220f7a05a3603b1))
* chore: Change license title ([`6d30b36`](https://github.com/sandialabs/staged-script/commit/6d30b365b7dcd41d520e693616d97e1bcaa1a3ac))

  Try updating the title of the LICENSE.md file to see if that fixes
  https://github.com/sandialabs/staged-script/security/code-scanning/33.
* chore(deps): Bump actions/upload-artifact from 3.1.3 to 4.3.3 ([`6495ca6`](https://github.com/sandialabs/staged-script/commit/6495ca6191d442311563ccabf2bae4c1bd494c2d))

  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 3.1.3 to 4.3.3.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/v3.1.3...65462800fd760344b1a7b4382951275a0abb4808)

  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump taskmedia/action-conventional-commits ([`ecd04f3`](https://github.com/sandialabs/staged-script/commit/ecd04f382664d4d8fb0987f0891d3606a8b49426))

  Bumps [taskmedia/action-conventional-commits](https://github.com/taskmedia/action-conventional-commits) from 1.1.3 to 1.1.17.
  - [Release notes](https://github.com/taskmedia/action-conventional-commits/releases)
  - [Changelog](https://github.com/taskmedia/action-conventional-commits/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/taskmedia/action-conventional-commits/compare/9148865058f63a6cb560ff4bfd7d534505f43646...866c0e6dba6aaaef9ad0939a40620b27888906c2)

  ---
  updated-dependencies:
  - dependency-name: taskmedia/action-conventional-commits
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump github/codeql-action from 2.25.11 to 3.25.11 ([`fa4143e`](https://github.com/sandialabs/staged-script/commit/fa4143ea9b8b5fd2cad1401a025f2118e8c4c1e8))

  Bumps [github/codeql-action](https://github.com/github/codeql-action) from 2.25.11 to 3.25.11.
  - [Release notes](https://github.com/github/codeql-action/releases)
  - [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/github/codeql-action/compare/v2.25.11...b611370bb5703a7efb587f9d136a52ea24c5c38c)

  ---
  updated-dependencies:
  - dependency-name: github/codeql-action
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/dependency-review-action from 2.5.1 to 4.3.3 ([`a626c8e`](https://github.com/sandialabs/staged-script/commit/a626c8ed293b08eb5566071a116d8e9b3803543f))

  Bumps [actions/dependency-review-action](https://github.com/actions/dependency-review-action) from 2.5.1 to 4.3.3.
  - [Release notes](https://github.com/actions/dependency-review-action/releases)
  - [Commits](https://github.com/actions/dependency-review-action/compare/0efb1d1d84fc9633afcdaad14c485cbbc90ef46c...72eb03d02c7872a771aacd928f3123ac62ad6d3a)

  ---
  updated-dependencies:
  - dependency-name: actions/dependency-review-action
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/checkout from 3.6.0 to 4.1.7 ([`5798a45`](https://github.com/sandialabs/staged-script/commit/5798a453544610313f5e01ebeadbe8501d822032))

  Bumps [actions/checkout](https://github.com/actions/checkout) from 3.6.0 to 4.1.7.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/v3.6.0...692973e3d937129bcbf40652eb9f2f61becf3332)

  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump actions/setup-python from 4.7.1 to 5.1.0 ([`e25de89`](https://github.com/sandialabs/staged-script/commit/e25de893d25b984055b697077f2e8d226c4f5504))

  Bumps [actions/setup-python](https://github.com/actions/setup-python) from 4.7.1 to 5.1.0.
  - [Release notes](https://github.com/actions/setup-python/releases)
  - [Commits](https://github.com/actions/setup-python/compare/65d7f2d534ac1bc67fcd62888c5f4f3d2cb2b236...82c7e631bb3cdc910f68e0081d67478d79c6982d)

  ---
  updated-dependencies:
  - dependency-name: actions/setup-python
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...

  Signed-off-by: dependabot[bot] <support@github.com>
* chore(deps): Bump ossf/scorecard-action from 2.3.1 to 2.3.3 ([`e915a86`](https://github.com/sandialabs/staged-script/commit/e915a864cbf9c93a1322c2f830853d84ca916ba6))

  Bumps [ossf/scorecard-action](https://github.com/ossf/scorecard-action) from 2.3.1 to 2.3.3.
  - [Release notes](https://github.com/ossf/scorecard-action/releases)
  - [Changelog](https://github.com/ossf/scorecard-action/blob/main/RELEASE.md)
  - [Commits](https://github.com/ossf/scorecard-action/compare/0864cf19026789058feabb7e87baa5f140aac736...dc50aa9510b46c811795eb24b2f1ba02a914e534)

  ---
  updated-dependencies:
  - dependency-name: ossf/scorecard-action
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...

  Signed-off-by: dependabot[bot] <support@github.com>

### Continuous integration
* ci: pre-commit auto-update ([`583f692`](https://github.com/sandialabs/staged-script/commit/583f692552a984cd81f8e867ea8db2c3808e52c9))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.3 → v0.7.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.3...v0.7.4)
* ci: pre-commit auto-update ([`9810c1c`](https://github.com/sandialabs/staged-script/commit/9810c1c15c71a755d64a928889b206bc8262b72a))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.2 → v0.7.3](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.2...v0.7.3)
* ci: pre-commit auto-update ([`0df05cd`](https://github.com/sandialabs/staged-script/commit/0df05cd1d523c95512652bcb99c6ec3aee76126f))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.1 → v0.7.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.1...v0.7.2)
* ci: pre-commit auto-update ([`2e89b5f`](https://github.com/sandialabs/staged-script/commit/2e89b5f1ef60edb10da99aadccb0e38c69f5bb5a))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.7.0 → v0.7.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.7.0...v0.7.1)
  - [github.com/gitleaks/gitleaks: v8.21.1 → v8.21.2](https://github.com/gitleaks/gitleaks/compare/v8.21.1...v8.21.2)
  - [github.com/pre-commit/mirrors-mypy: v1.12.1 → v1.13.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.12.1...v1.13.0)
* ci: pre-commit auto-update ([`f552714`](https://github.com/sandialabs/staged-script/commit/f552714bd7b739cf9da389a306cb910b966478ec))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.9 → v0.7.0](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.9...v0.7.0)
  - [github.com/gitleaks/gitleaks: v8.20.1 → v8.21.1](https://github.com/gitleaks/gitleaks/compare/v8.20.1...v8.21.1)
  - [github.com/pre-commit/mirrors-mypy: v1.11.2 → v1.12.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.2...v1.12.1)
* ci: pre-commit auto-update ([`533c179`](https://github.com/sandialabs/staged-script/commit/533c1795be6ca0824bb0cc0df239260283a21deb))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.8 → v0.6.9](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.8...v0.6.9)
  - [github.com/gitleaks/gitleaks: v8.19.3 → v8.20.1](https://github.com/gitleaks/gitleaks/compare/v8.19.3...v8.20.1)
  - [github.com/pre-commit/pre-commit-hooks: v4.6.0 → v5.0.0](https://github.com/pre-commit/pre-commit-hooks/compare/v4.6.0...v5.0.0)
* ci: pre-commit auto-update ([`a3be6f7`](https://github.com/sandialabs/staged-script/commit/a3be6f7b221d0e2937a09f51c0f2012559aea82d))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.7 → v0.6.8](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.7...v0.6.8)
  - [github.com/gitleaks/gitleaks: v8.19.2 → v8.19.3](https://github.com/gitleaks/gitleaks/compare/v8.19.2...v8.19.3)
* ci: pre-commit auto-update ([`4d97575`](https://github.com/sandialabs/staged-script/commit/4d97575aba0a9c6b561e2a39d6e004569081d860))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.5 → v0.6.7](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.5...v0.6.7)
* ci: pre-commit auto-update ([`f397d17`](https://github.com/sandialabs/staged-script/commit/f397d179deb374c194c8c337ead8ec67d9057a08))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.4 → v0.6.5](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.4...v0.6.5)
  - [github.com/gitleaks/gitleaks: v8.18.4 → v8.19.2](https://github.com/gitleaks/gitleaks/compare/v8.18.4...v8.19.2)
* ci: pre-commit auto-update ([`e0e303d`](https://github.com/sandialabs/staged-script/commit/e0e303d7dde1bbd934072ab06f1f148205b33f12))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.3 → v0.6.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.3...v0.6.4)
* ci: pre-commit auto-update ([`5dd02a0`](https://github.com/sandialabs/staged-script/commit/5dd02a0258bdfef3913b3d538351f56f6f2a5179))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.2 → v0.6.3](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.2...v0.6.3)
  - [github.com/PyCQA/doc8: v1.1.1 → v1.1.2](https://github.com/PyCQA/doc8/compare/v1.1.1...v1.1.2)
* ci: pre-commit auto-update ([`d19aafd`](https://github.com/sandialabs/staged-script/commit/d19aafd8ff459b735db02a818b4a7c479a362e44))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.6.1 → v0.6.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.6.1...v0.6.2)
  - [github.com/pre-commit/mirrors-mypy: v1.11.1 → v1.11.2](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.1...v1.11.2)
* ci: pre-commit auto-update ([`6145bc3`](https://github.com/sandialabs/staged-script/commit/6145bc3acffd0cfa71c89364dc3896c1f2bc14c9))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.7 → v0.6.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.7...v0.6.1)
* ci: pre-commit auto-update ([`48e884b`](https://github.com/sandialabs/staged-script/commit/48e884bf267aabadecad2728e439007c081f6fe8))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.6 → v0.5.7](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.6...v0.5.7)
* ci: pre-commit auto-update ([`6a5861b`](https://github.com/sandialabs/staged-script/commit/6a5861bfe54c61b3f470a2be5536c5412179860f))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.5 → v0.5.6](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.5...v0.5.6)
  - [github.com/pre-commit/mirrors-mypy: v1.11.0 → v1.11.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.0...v1.11.1)
* ci: pre-commit auto-update ([`6fe6f06`](https://github.com/sandialabs/staged-script/commit/6fe6f0677a533c21bf75de3fe98ac7d4b36bfa51))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.4 → v0.5.5](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.4...v0.5.5)
* ci: pre-commit auto-update ([`4f6af56`](https://github.com/sandialabs/staged-script/commit/4f6af56c982f63a162a4503ed9e92f8da0e543ff))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.2 → v0.5.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.2...v0.5.4)
  - [github.com/pre-commit/mirrors-mypy: v1.10.1 → v1.11.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.10.1...v1.11.0)
* ci: pre-commit auto-update ([`72577d3`](https://github.com/sandialabs/staged-script/commit/72577d3becd9303c028e80fd037605335d4c6988))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.1 → v0.5.2](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.1...v0.5.2)
* ci: pre-commit auto-update ([`53a27bf`](https://github.com/sandialabs/staged-script/commit/53a27bf0f60d0fc9dfa35a1ecba139eec8ccb347))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.5.0 → v0.5.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.0...v0.5.1)
  - [github.com/gitleaks/gitleaks: v8.16.3 → v8.18.4](https://github.com/gitleaks/gitleaks/compare/v8.16.3...v8.18.4)
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
* ci: pre-commit auto-update ([`452fb68`](https://github.com/sandialabs/staged-script/commit/452fb6884d9f3674a70f891431e9c2baf2cc9f41))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.10 → v0.5.0](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.10...v0.5.0)
  - [github.com/pre-commit/mirrors-mypy: v1.10.0 → v1.10.1](https://github.com/pre-commit/mirrors-mypy/compare/v1.10.0...v1.10.1)
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
  intended to be used.  This commit brings things into conformity with
  how `argparse` is intended to be used, specifying a one-word group name,
  followed by a more detailed group description.
* fix!: Handle --dry-run correctly ([`8f436af`](https://github.com/sandialabs/staged-script/commit/8f436af8529623ce8e0f929aaae191c670d444a1))

  When a `DriverScript` subclass is run in dry-run mode, instead of
  executing commands in the shell, print a message indicating what would
  have been run.  Prior to this, `DriverScript` provided the flag, but
  relied on subclass developers to ensure commands weren't run.  This was
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
  shell as a string rather than a list of strings.  It just seemed like a
  better interface, to make it easy for the user writing their Python
  scripts to simply wrap their bash commands.  However, this opens up a
  danger for bad actors to cause problems via command injection.  We can
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
* ci: pre-commit auto-update ([`11cc2e1`](https://github.com/sandialabs/staged-script/commit/11cc2e1c7e245bd45c83667b05bd5501031b4e64))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.9 → v0.4.10](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.9...v0.4.10)
* ci: pre-commit auto-update ([`ff4203a`](https://github.com/sandialabs/staged-script/commit/ff4203aa7c7fe124b38d020dbf4d5ff0bef464f8))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.8 → v0.4.9](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.8...v0.4.9)
* ci: pre-commit auto-update ([`66eb281`](https://github.com/sandialabs/staged-script/commit/66eb2818988068c80e597336b78692df50333af1))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.7 → v0.4.8](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.7...v0.4.8)
* ci: Add ReadTheDocs configuration ([`40f08f2`](https://github.com/sandialabs/staged-script/commit/40f08f2c8a52e1181ca7b8ae473754abcfd54bf1))
* ci: Don't fail fast ([`0d3a5e3`](https://github.com/sandialabs/staged-script/commit/0d3a5e3a2a1b41d8dc11a3c7b7ec2a4a67c9fd98))

  If one job in the matrix of jobs fails, we still want to be able to see
  the results from the other jobs.
* ci: Stub out workflow ([`c2ab413`](https://github.com/sandialabs/staged-script/commit/c2ab4134bc2f53dd502e6df5996a7f0ad3d06931))
* ci: Add OpenSSF Scorecard workflow ([`f2904b7`](https://github.com/sandialabs/staged-script/commit/f2904b7318c3874a1b2694bb5085b63c8a0c7179))
* ci: pre-commit auto-update ([`82b4201`](https://github.com/sandialabs/staged-script/commit/82b4201636876ba782693abd0e271c0aa2193341))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.5 → v0.4.7](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.5...v0.4.7)
* ci: pre-commit auto-update ([`099b7e6`](https://github.com/sandialabs/staged-script/commit/099b7e6e58604e75e07b9789aa2e4d7701029df7))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.4 → v0.4.5](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.4...v0.4.5)
* ci: pre-commit auto-update ([`47ba3b7`](https://github.com/sandialabs/staged-script/commit/47ba3b7caa75f34fb08c82433fedc311a0a8181a))

  updates:
  - [github.com/astral-sh/ruff-pre-commit: v0.4.1 → v0.4.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.4.1...v0.4.4)
  - [github.com/pre-commit/mirrors-mypy: v1.9.0 → v1.10.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.9.0...v1.10.0)
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
  rather than determining them on the fly.  This is useful for things like
  the script execution summary.

  Also add a unit test for `raise_parser_error()`, which was accidentally
  omitted in a prior commit.
* feat: Add help formatter to package ([`b458d95`](https://github.com/sandialabs/staged-script/commit/b458d959005422788646899a5cf70b91e04957ab))

  Add a class to the `driver_script` package to use as a formatter class
  for the `DriverScript` `ArgumentParser`.  Make it such that the parser
  description is treated as raw text (no automatic formatting is done),
  and show the default values for all arguments.
* feat: Add flag for printing commands ([`7a7a0e0`](https://github.com/sandialabs/staged-script/commit/7a7a0e0cc386e35698da4d0c5433e4d18091e828))

  Add a flag when instantiating a `DriverScript` to govern whether
  commands should be printed immediately before running them.  Default it
  to `True` for backwards compatibility.  Also provide a keyword argument
  to the `run()` method that, if specified, will override the class flag.
  In this way users could, e.g., instantiate a `DriverScript`, telling it
  to print all commands, and then specify that certain commands should not
  be printed.  The opposite of this is also possible (e.g., don't print
  any commands, except this one and that one).
* feat: Add raise_parser_error ([`0f60f8d`](https://github.com/sandialabs/staged-script/commit/0f60f8d9bc8c80e3529a8e7abb69b8e76da4e480))

  Add a method to the `DriverScript` base class to raise a parser error
  when a user has done something wrong in specifying the command line
  arguments.  This differs from `argparse.ArgumentParser.error()` in that
  it's a little more user friendly, printing the help text first, and then
  the particular error in yellow.
* feat: Capture script success/failure ([`68ea1ae`](https://github.com/sandialabs/staged-script/commit/68ea1ae93532e58da8d96e0e3a36381d2551295b))

  Provide an instance attribute to allow subclass developers to toggle
  whether the script has succeeded or failed, and include the result in
  the script execution summary.
* feat!:  Add stage retry functionality ([`d27ce6f`](https://github.com/sandialabs/staged-script/commit/d27ce6fed864fa7935d6f636c201b1733c85f34f))

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
  functionality outside of this.  The safest thing will be for subclass
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
  actions to run after a stage ends.  These can be specified for all
  stages, and they can also optionally be customized on a stage by stage
  basis.
* feat: Allow custom "begin stage" phases ([`f05a5d4`](https://github.com/sandialabs/staged-script/commit/f05a5d47c03e86ad650307c02eefaa903f4d9e04))

  Provide subclass developers with the flexibility to specialize the
  "begin stage" actions on a stage by stage basis.
* feat: Add pre-stage actions ([`fb6d51e`](https://github.com/sandialabs/staged-script/commit/fb6d51e98797280e432423eb344f88c3d520100e))

  Add the flexibility to allow subclass designers to specify pre-stage
  actions to run before a stage begins.  These can be specified for all
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
  (e.g., if something failed).  Introduce a `StageDuration` class that
  inherits from `NamedTuple`, such that the entries added to the list must
  always be a `(str, timedelta)` `tuple` that will from then on be
  immutable and allow easy member access via dot notation.

### Refactoring
* refactor: Use functools.cached_property instead ([`3d91282`](https://github.com/sandialabs/staged-script/commit/3d91282518331e91c650f6c76815b2cf5b18e030))

  This package was originally developed for Python 3.6, before
  `functools.cached_property` was introduced.  That should be a drop-in
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
  easier to understand.  No functional changes; just cut from here, paste
  to there.  Also prefix some methods with `_` to indicate they're only
  intended for internal use.
* refactor!: Stages no longer registered by default ([`b3ac262`](https://github.com/sandialabs/staged-script/commit/b3ac2625abc12f88b5549926e1c1788e648a1c2c))

  Since its inception, `DriverScript`'s `stage` decorator has attempted
  to capture all the `stage`s defined by `DriverScript` subclasses in the
  `stages` class variable automatically.  The desire was to keep things as
  easy as possible for subclass developers, in that all they'd need to do
  was inherit from `DriverScript`, define some methods decorated with
  `stage`, and then `DriverScript` would automatically handle things like
  stage-specific arguments (retries, etc.) and methods (pre/post,
  begin/end, etc.).  Unfortunately this feature has been a thorn in our
  side for development, due to, e.g., `pytest` multiple-loading modules
  (and therefore redefining stages), `DriverScript` subclass hierarchies,
  etc.

  In order to pave the way for the flexibility for one `DriverScript`
  subclass to use stages defined within a separate `DriverScript`
  subclass, this commit makes it such that stages are no longer
  automatically registered.  Instead subclass developers must pass the set
  of stages to register into the constructor when instantiating an object.
  This is a minor inconvenience, but it removes a good deal of hacky code
  and makes it such that `DriverScript` subclasses are decoupled from one
  another, so we believe the change is well worth it in the long run.

  Note that this is a breaking change, as all subclasses must be update
  their constructor definitions and any instantiations.
* refactor!: Switch stages to standard set ([`525fd79`](https://github.com/sandialabs/staged-script/commit/525fd792f39b70ae2cf6e6232fb270b70d6f9851))

  Initially the `stages` attribute of a `DriverScript` class was
  implemented as an ordered set (which in Python is a value-less `dict`
  converted to a `list`).  The thinking there was that a `DriverScript`
  subclass should define a series of stages in order and they would be
  executed in that order.  However, this failed to consider the following
  use case:  Class `A` inherits from `DriverScript` and defines a few
  stages, then class `B` inherits from `A` and defines few more, but the
  intended sequence of stages isn't all from `A` followed by all from `B`;
  instead, they're meant to be interspersed.  Since this is a valid use
  case, it makes sense to switch `stages` over to a standard `set`.

  Another motivation for the `stages` being an ordered set was considering
  the possibility of wanting to return to a prior stage if a certain stage
  failed.  Consider an example `DriverScript` subclass with stages to
  configure, build, and test a code.  If the test stage fails, perhaps the
  failure was seemingly random, and it'd be worthwhile to automatically
  rewind and retry the build and test stages again before notifying anyone
  of the failure.  Or perhaps a certain regex match in the test output
  indicates you should rewind further and reconfigure.  However, after
  further reflection, allowing such flexibility would open up a can of
  worms that probably shouldn't be opened.  `DriverScript` already allows
  a subclass developer to automatically retry a stage.  If something's
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
  in the `_begin_stage` method.  Use `current_stage` in place of the
  `stage_name` passed into the wrapper, where appropriate.

  Note that this is a breaking change, as it changes the signature for the
  `_begin_stage` method.
* refactor: Get phase method rather than running it ([`8af3f75`](https://github.com/sandialabs/staged-script/commit/8af3f755db304b827fb358f60f848bed8fb07b01))

  In preparation for adding automatic retry functionality to the `stage`
  decorator, rewrite the `run_phase` method such that instead of running
  the method corresponding to the phase, it simply returns the `Callable`,
  which is then run outside the function.  This generalization will make
  it such that we can pass a phase method to the `Retrying` object when
  we're ready for that.
* refactor: Wrap retryable phases into a function ([`345b77c`](https://github.com/sandialabs/staged-script/commit/345b77c0faf2fcdb98f4a90408b2981205b575f7))

  In preparation for adding automatic retry functionality to the stage
  decorator, wrap the phases that are to be retried into a function so
  they're easy to call together.
* refactor!: Stages always return None ([`b1238be`](https://github.com/sandialabs/staged-script/commit/b1238be88d25f0cb7225287544dbecda1c6b4a35))

  In preparation for adding stage retry functionality, make it such that a
  function decorated with `DriverScript.stage` must return `None`.  This
  is reasonable because a conceptual stage of a script *does* something,
  but doesn't *return* something.

  Note that this is a breaking change for `DriverScript`, as any
  subclasses relying on returning values from functions decorated with
  `stage` will no longer work.  A follow-up commit will fix this problem
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
  parsing the command line argument supplied by the base class.  This will
  be overridden and extended by child classes.
* refactor: Add parser property to base class ([`1c4f10f`](https://github.com/sandialabs/staged-script/commit/1c4f10fae8ca5843c026c8fc8ef3103db1c094d4))

  Add a `parser` lazily-evaluated property to the `DriverScript` base
  class to handle parsing of arguments supplied by the base class.  This
  will be overridden and extended by child classes.
* refactor: Use Rich Table for timing report ([`1d24cd1`](https://github.com/sandialabs/staged-script/commit/1d24cd1d6c17602925ced11dc87900046f1ca3d5))

  Rather than generating the timing report table manually, use
  `rich.table.Table` to handle the magic automatically.  Also abandon the
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

### Unknown
* Merge branch 'driver-script-switch-stages-to-set' into 'develop' ([`9157e38`](https://github.com/sandialabs/staged-script/commit/9157e3813c70f7815e2f993a89b3be185f8b4856))

  refactor!(DriverScript): Switch stages to standard set

  See merge request gms/gms-common!10807
* Merge branch 'driver-script-retry-stage-exception' into 'develop' ([`10783ae`](https://github.com/sandialabs/staged-script/commit/10783ae0de7b52f282d6656630a036bb3eaf5cae))

  DriverScript: Create RetryStage exception

  See merge request gms/gms-common!10742
* Merge branch 'driver-script-custom-help-formatter' into 'develop' ([`928203c`](https://github.com/sandialabs/staged-script/commit/928203c2aeb16f7aa03d4e43160f4fef107c40df))

  DriverScript: Add help formatter to package

  See merge request gms/gms-common!10688
* Merge branch 'driver-script-fix-help-text' into 'develop' ([`e04abe6`](https://github.com/sandialabs/staged-script/commit/e04abe62e9457242ba69782988d3bc4c78fda611))

  DriverScript: Fix retry group help text

  Closes #2272

  See merge request gms/gms-common!10685
* Merge branch '2216-fix-how-driver-script-handles-dry-run' into 'develop' ([`f94c3fd`](https://github.com/sandialabs/staged-script/commit/f94c3fd51d272418e44e49f07ca719551b665cd0))

  Fix how DriverScript handles --dry-run

  Closes #2216

  See merge request gms/gms-common!10576
* Merge branch 'move-script-success-to-driver-script' into 'develop' ([`6e1f46e`](https://github.com/sandialabs/staged-script/commit/6e1f46e007302467f231877f4bcbce8cab3ed7d2))

  Move script_success to DriverScript

  Closes #2215

  See merge request gms/gms-common!10574
