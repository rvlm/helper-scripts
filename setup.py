#!/usr/bin/env python
import os
import sys
from setuptools import setup

# Damn you Guido.
assert sys.version_info.major >= 3, "Python 2.* is not supported"


def slurp(filename):
    """
    Return whole file contents as string. File is searched relative to
    directory where this `setup.py` is located.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name               = "rvlm.labhelpers",
    version            = "0.1.0.0",
    packages           = ["rvlm", "rvlm.labhelpers"],
    namespace_packages = ["rvlm"],
    package_dir        = {'': "src"},
    author             = "Pavel Kretov",
    author_email       = "firegurafiku@gmail.com",
    license            = "MIT",
    url                = "https://github.com/rvlm/rvlm-labhelpers",
    keywords           = ["helpers"],
    requires           = ["numpy", "rvlm.entrypoint"],
    description        = ("Helper library and scripts which were useful for "
                          "my experiments at the lab #426 (devoted to UWB "
                          "signals and antennas) during my PhD at Voronezh "
                          "State University."),
    classifiers        = ["Programming Language :: Python",
                          "Programming Language :: Python :: 3",
                          "Development Status :: 2 - Pre-Alpha",
                          "Environment :: Console",
                          "Intended Audience :: Developers",
                          "Intended Audience :: Science/Research",
                          "License :: OSI Approved :: MIT License",
                          "Natural Language :: English",
                          "Operating System :: POSIX" ],
    long_description   = slurp("README.rst"))
