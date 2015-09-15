#!/usr/bin/env python
import os
from setuptools import setup


def slurp(filename):
    """
    Return whole file contents as string. File is searched relative to
    directory where this `setup.py` is located.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


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
