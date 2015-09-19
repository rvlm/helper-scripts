# -*- coding: utf-8 -*-
"""
`rvlm.labhelpers.trivia`: trivial things Python lacks
=====================================================

This is a helper module, providing some trivial, but still useful and
convenient helper functions, which are absent from the standard library for
some reason. Not all of them may be a good idea, thought, and none of them
claims to be the pythonic™ way to do things.

Many of the module function try to resemble things widely used in functional
languages, like :func:`head`.

:copyright: 2015, Pavel Kretov
:license: MIT
"""


def ipairs(iterable):
    """

    :param iterable:
    :return:

        >>> for i, v in ipairs(["foo", "bar", "qux"]): print(i, v)
        0 foo
        1 bar
        2 qux
        >>> for i, v in ipairs(range(3)): print(i, v)
        0 0
        1 1
        2 2

    """
    i = 0
    for v in iterable:
        yield (i, v)
        i += 1


def omit_empty_items(sequence):
    """
    Filters out sequence items which are :const:`None` or empty. If argument is
    :const:`None` than the return value is :const:`None` too, but if argument
    is an empty sequence, another empty sequence is returned.
    """
    return None if sequence is None \
        else filter(lambda x: (x is not None) and (len(x) != 0), sequence)


def tuple1(lst):
    """
    Converts list to tuple or single value. If argument `lst` is a list
    (or other enumerable) holding more than one item, then this function
    returns a tuple with the same values with their original order preserved.
    If argument hold only single value, that value itself is returned.
    """
    ts = tuple(lst)
    if len(ts) == 0: return None
    if len(ts) == 1: return ts[0]
    return ts


def head(sequence):
    """
    Returns first item from `sequence` or :const:`None` if sequence is empty.
    """
    try:
        return iter(sequence).next()
    except StopIteration:
        return None


def applyfs(funcs, args):
    """
    Applies several functions to single set of arguments. This function takes
    a list of functions, applies each to given arguments, and returns the list
    of obtained results. For example:

        >>> from operator import add, sub, mul
        >>> list(applyfs([add, sub, mul], (10, 2)))
        [12, 8, 20]

    :param funcs: List of functions.
    :param args:  List or tuple of arguments to apply to each function.
    :return:      List of results, returned by each of `funcs`.
    """
    return map(lambda f: f(*args), funcs)


def unpackf(func):
    """
    Wraps `func` with argument unpacker. Thus the function can be called with
    all its arguments combined into a single list. It's easier to explain this
    by example:

        >>> def f(x, y, z): return x + y + z
        >>> unpackf(f)([1, 2, 3])
        6

    This feature is particularly useful with `numpy.apply_along_axis` function
    which expect its function to take a single list as argument.

        >>> import numpy
        >>> import operator
        >>> a = numpy.array([[1, 2], [3, 4]])
        >>> numpy.apply_along_axis(sum, 0, a)
        array([4, 6])
        >>> numpy.apply_along_axis(unpackf(operator.add), 0, a)
        array([4, 6])

    :param func: Callable object, taking a number of positional parameters.
    :return:     Wrapper function, taking a single list parameter.
    """
    return (lambda args: func(*args))
