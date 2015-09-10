# -*- coding: utf-8 -*-
"""
rvlm.labhelpers.extdict: helper routines for Python built-in dictionaries
=========================================================================

This is a helper module, extending python built-in dictionaries (or anything
following their interface) in way the Python itself lacks for some reasons.
Those reason may be different: the routines may be not very pythonic by their
nature, nobody thought that's a good idea to add something like them into the
standard library, or anything.

For example, this module has `mapk` and `mapv` functions which help avoiding
unnecessary loops over dictionary in the code, while pure pythonostas prefer
dictionary comprehension instead. Moreover, their names are not very pythonic
too, but they're short and concise, and do their work.

:copyright: 2015, Pavel Kretov
:license: MIT
"""
import re
from rvlm.labhelpers.trivia import tuple1


def mapk(f, dic):
    """
    Maps dictionary keys against function `f`. Given that original `dic` is
    `k → v` mapping, this function returns another dictionary `f(k) → v`. If
    `f` doesn't produce unique result for each key present in `dic`, then an
    exception is raised.
    """
    result = {}
    for k, v in dic.iteritems():
        result[f(k)] = v

    return result


def mapv(f, dic):
    """
    Maps dictionary values against function `f`. Just like :func:`mapk`, this
    function converts `k → v` dictionary into `k → f(v)`.
    """
    result = {}
    for k, v in dic.iteritems():
        result[k] = f(v)

    return result


def extract_keys(dic, pattern, keytypes=float):
    """
    Rebuilds dictionary by extracting numbers from its keys. This function
    tries to match each key (which must be a string value) against given
    `pattern`. Then all matched items are gathered into another dictionary,
    with string keys converted into number tuples.

    Pattern should contain at least one `{}` placeholder, denoting a number to
    be extracted. If two or more placeholders are given, they are extracted
    into a tuple. See some examples:

        ...

    """
    pattern = re.escape(pattern)
    pattern = pattern.replace(re.escape("{}"), "([\\d.Ee+-]+)")
    phi_rex = re.compile(pattern)

    def extract_key(name):
        match = phi_rex.match(name)
        if not match:
            return None

        if type(keytypes) == tuple:
            keys = [f(g) for f, g in zip(keytypes, match.groups())]
            return tuple1(keys)
        else:
            return keytypes(match.group(1))

    result = {}
    for name, value in dic.items():
        key = extract_key(name)
        if key is not None:
            result[key] = value

    return result
