#!/usr/bin/env python
from setuptools import setup
from setuptools.command.test import test as TestCommand
import os
import sys

# Utility function to read whole file contents.
def filecontents(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

# Helpful class for pytest integration. It was taken without modifications
# from https://pytest.org/latest/goodpractises.html.
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args  = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        if errno != 0:
            sys.exit(errno)

setup(
    name          = "rvlm.labhelpers",
    packages      = ["rvlm", "rvlm.labhelpers"],
    namespace_packages = ["rvlm"],
    version       = "0.0.6",
    description   = (
        "Various helper script (and and a helper library) which were useful"
        "for my experiments in the lab #426 (devoted to ultra-wideband signals "
        "and antennas) during my PhD at Voronezh State University."),
    author        = "Pavel Kretov",
    author_email  = "firegurafiku@gmail.com",
    license       = "MIT",
    url           = "https://github.com/rvlm/rvlm-labhelpers",
    keywords      = ["helpers"],
    classifiers   = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Topic :: Software Development :: Libraries :: Python Modules" ],
    long_description = filecontents("README.rst"),
    tests_require = ['pytest'],
    cmdclass      = {'test': PyTest})
