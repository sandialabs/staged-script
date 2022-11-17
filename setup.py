#!/usr/bin/env python3
from setuptools import setup

setup(
    name="driver_script",
    version="0.1.0",
    description=(
        "A base class to inherit from when building scripts that are intended "
        "to driver a series of commands executed in the underlying shell."
    ),
    packages=["driver_script"],
    scripts=[],
    python_requires=">=3.10",
    tests_require=["pytest==7.1.1"],
    install_requires=["rich==12.5.1"]
)
