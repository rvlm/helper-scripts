#!/usr/bin/env python
from setuptools import setup
from setuptools.command.test import test as TestCommand
import os
import sys


# Utility function to read whole file contents.
def slurp(fname):
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
    name               = "rvlm.labhelpers",
    version            = "0.0.6",
    packages           = ["rvlm", "rvlm.labhelpers"],
    namespace_packages = ["rvlm"],
    package_dir        = {'': "src"},
    author             = "Pavel Kretov",
    author_email       = "firegurafiku@gmail.com",
    license            = "MIT",
    url                = "https://github.com/rvlm/rvlm-labhelpers",
    keywords           = ["helpers"],
    requires           = ["numpy", "rvlm.entrypoint"],
    tests_require      = ['pytest'],
    cmdclass           = {'test': PyTest},
    description        = ("Helper library and scripts which were useful for "
                          "my experiments at the lab #426 (devoted to UWB "
                          "signals and antennas) during my PhD at Voronezh "
                          "State University."),
    classifiers        = ["Programming Language :: Python",
                          "Programming Language :: Python :: 2.6",
                          "Programming Language :: Python :: 2.7",
                          "Programming Language :: Python :: 3",
                          "Development Status :: 2 - Pre-Alpha",
                          "Environment :: Console",
                          "Intended Audience :: Developers",
                          "Intended Audience :: Science/Research",
                          "License :: OSI Approved :: MIT License",
                          "Natural Language :: English",
                          "Operating System :: POSIX" ],
    long_description   = slurp("README.rst"))
