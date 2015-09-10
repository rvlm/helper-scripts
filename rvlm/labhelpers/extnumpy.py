import numpy
from functools              import partial
from rvlm.labhelpers.trivia import applyfs, unpackf

def array2d(data):
    """

    :param data:
    :return:
    """
    arr = numpy.array(data, ndmin=2)
    if len(arr.shape) != 2:
        raise ValueError("Wrong input array shape")

    if arr.shape[0] == 1 and arr.shape[1] > 1:
        return arr.transpose()

    return arr

def hstack_skip_empty(*arrays):
    return numpy.hstack(tuple(filter(lambda a: a.size > 0, arrays)))

def filter_along_axis(pred, axis, array):
    """ http://stackoverflow.com/a/26154854/1447225
    """
    bool_array = numpy.apply_along_axis(pred, axis, array)
    return array[bool_array]

def tabularf(array, funcs = []):
    """
    """
    args  = array2d(array)
    fvals = numpy.apply_along_axis(partial(applyfs, funcs), 1, array)
    return hstack_skip_empty(args, fvals)

def tabulardf(dic, funcs = []):
    """
    """
    args  = array2d(dic.keys())
    vals  = array2d(dic.values())
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
        >>> extnumpy.tabularf([xs, ys])
        array([[ 0.,  2.],
               [ 1.,  2.],
               [ 0.,  3.],
               [ 1.,  3.]])

        >>> extnumpy.tabularf([xs, ys], [operator.add, operator.mul])
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

    baxes = numpy.array(list(numpy.broadcast(*axes)))
    return numpy.apply_along_axis(appendf, 1, baxes)
