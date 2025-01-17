#!/usr/bin/env python

import setuptools


def readme_contents() -> str:
    with open('README.md', 'r') as fd:
        src = fd.read()
    return src


_classifiers = """
Programming Language :: Python :: 3
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Natural Language :: English
Programming Language :: Other
Programming Language :: C++
Topic :: Scientific/Engineering :: Information Analysis
"""

setuptools.setup(
    name='cmdstanpy',
    version='0.9',
    description='Python interface to CmdStan',
    long_description=readme_contents(),
    long_description_content_type="text/markdown",
    author='Stan Dev Team',
    url='https://github.com/stan-dev/cmdstanpy',
    packages=['cmdstanpy'],
    install_requires='numpy filelock'.split(),
    classifiers=_classifiers.strip().split('\n'),
)
