"""

"""
import numpy
from functools                import partial
from rvlm.labhelpers.trivia   import applyfs
from rvlm.labhelpers.extnumpy import hstack_skip_empty


def tabular(data):
    """
    Converts data into a two-dimensional table. In fact, this function is just
    a wrapper over :func:`numpy.array` with the following minor changes:

        - :func:`tabular` limits its usage to 1D and 2D `data` only;
        - if `data` is a 1D array, a 2D table still returned, in a *vertically*
          stacked manner.

    This behavior may seem odd, but in fact it's more consistent than
    `numpy.array(data, ndmin=2)`, as data is always laid out vertically.
    Compare the following examples:

        >>> tabular([1, 2, 3])
        array([[1],
               [2],
               [3]])
        >>> numpy.array([1, 2, 3], ndmin=2)
        array([[1, 2, 3]])

    But in the following code both `tabular` and `numpy.array` would produce
    the results:

        >>> tabular([(1, 2), (3, 4), (5, 6)])
        array([[1, 2],
               [3, 4],
               [5, 6]])
        >>> tabular([[1, 2, 3], [4, 5, 6]])
        array([[1, 2, 3],
               [4, 5, 6]])

    :param data:
    :return:
    :raise ValueError:
    """
    arr = numpy.array(data, ndmin=2)
    if len(arr.shape) != 2:
        raise ValueError("Wrong input array shape")

    if arr.shape[0] == 1 and arr.shape[1] > 1:
        return arr.transpose()

    return arr


def tabularf(data, funcs = []):
    """
    Converts data into a two-dimentional table, with additional columns. These
    columns are obtained as the result of `funcs` evaluation on the rows of
    original data. Examples can explain this better:

        >>> import operator
        >>> tabularf([1, 2, 3, 4], [operator.neg])
        array([[ 1, -1],
               [ 2, -2],
               [ 3, -3],
               [ 4, -4]])
        >>> tabularf([[1, 2], [3,4]], [operator.add, operator.mul])
        array([[ 1,  2,  3,  2],
               [ 3,  4,  7, 12]])

    :param data:
    :param funcs:
    :return:
    """
    args  = tabular(data)
    fvals = numpy.apply_along_axis(lambda vals: list(applyfs(funcs, vals)), 1, args)
    return hstack_skip_empty(args, fvals)


def tabulardf(dic, funcs = []):
    """
    """
    args  = tabular(dic.keys())
    vals  = tabular(dic.values())
    fvals = numpy.apply_along_axis(partial(applyfs, funcs), 1, args)
    return hstack_skip_empty(args, vals, fvals)


def tabularmf(axes, funcs = []):
    """
    Produces list of points for an N-dimentional mesh grid. This table can also
    be extended with values of arbitrary functions computed on the points. For
    example:

        >>> import numpy
        >>> import operator
        >>> xspace = numpy.linspace(0, 1, num=2)
        >>> yspace = numpy.linspace(2, 3, num=2)
        >>> [xs, ys] = numpy.meshgrid(xspace, yspace)
        >>> tabularmf([xs, ys])
        array([[ 0.,  2.],
               [ 1.,  2.],
               [ 0.,  3.],
               [ 1.,  3.]])

        >>> tabularmf([xs, ys], [operator.add, operator.mul])
        array([[ 0.,  2.,  2.,  0.],
               [ 1.,  2.,  3.,  2.],
               [ 0.,  3.,  3.,  0.],
               [ 1.,  3.,  4.,  3.]])

    This method is especially useful for saving multidimentional data in a form
    readable by a human. Use :func:`numpy.savetxt` for actual saving to file.
    """
    def appendf(args):
        fvals = [f(*args) for f in funcs]
        return list(args) + fvals

    broadcasted_axes = numpy.array(list(numpy.broadcast(*axes)))
    return numpy.apply_along_axis(appendf, 1, broadcasted_axes)


def sorted_rows(table, fields=None):
    """

        >>> t = tabular([[64, 77,  6], \
                         [77,  3, 22], \
                         [30, 30, 79]])
        >>> sorted_rows(t)
        array([[30, 30, 79],
               [64, 77,  6],
               [77,  3, 22]])

    :param table:
    :return:
    """
    return tabular(sorted(table.tolist()))


def sorted_cols(table):
    """

        >>> t = tabular([[64, 77,  6], \
                         [77,  3, 22], \
                         [30, 30, 79]])
        >>> sorted_cols(t)
        array([[ 6, 64, 77],
               [22, 11,  3],
               [79, 30, 30]])


    :param table:
    :return:
    """
    raise NotImplementedError()