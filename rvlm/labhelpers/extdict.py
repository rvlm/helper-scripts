# -*- coding: utf-8 -*-
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
    Rebuilds dictionary by extracting numbers from its keys. This function tries
    to match each key (which must be a string value) against given `pattern`.
    Then all matched items are gathered into another dictionary, with string
    keys converted into number tuples.

    Pattern should contain at least one `{}` placeholder, denoting a number to
    be extracted. If two or more placeholders are given, they are extracted into
    a tuple. See some examples:

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
