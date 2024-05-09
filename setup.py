"""
Setup file for the ``staged-script`` package.

To install, simply ``python3 -m pip install .`` in the repository root.
"""

from setuptools import setup

setup(
    name="staged-script",
    version="1.0.0",
    description=(
        "A base class to inherit from when building scripts that are "
        "subdivided into a series of stages."
    ),
    packages=["staged_script"],
    scripts=[],
    python_requires=">=3.10",
    tests_require=["pytest==7.1.1"],
    install_requires=["rich==12.5.1"],
)
