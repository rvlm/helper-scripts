"""

"""
import numpy


def hstack_skip_empty(*arrays):
    """

        >>> a = numpy.array([1, 2, 3], ndmin=2).T
        >>> b = numpy.array([4, 5, 6], ndmin=2).T
        >>> c = numpy.array([],        ndmin=2).T
        >>> hstack_skip_empty(a, c, b)
        array([[1, 4],
               [2, 5],
               [3, 6]])

    """
    return numpy.hstack(tuple(filter(lambda a: a.size > 0, arrays)))


def vstack_skip_empty(*arrays):
    """

        >>> a = numpy.array([1, 2, 3], ndmin=2)
        >>> b = numpy.array([4, 5, 6], ndmin=2)
        >>> c = numpy.array([],        ndmin=2)
        >>> vstack_skip_empty(a, c, b)
        array([[1, 2, 3],
               [4, 5, 6]])

    """
    return numpy.vstack(tuple(filter(lambda a: a.size > 0, arrays)))


def filter_along_axis(pred, axis, array):
    """ http://stackoverflow.com/a/26154854/1447225
    """
    bool_array = numpy.apply_along_axis(pred, axis, array)
    return array[bool_array]


def regular_meshgrid(ranges, shape):
    """
    Generates regular equidistant N-dimensional mesh grid.
    This function is kind of generalization for `numpy.linspace`, which takes
    lists instead of scalar range parameters.

    :param ranges: List of `(start, stop)` tuples for each dimension.
    :param shape:  List of `num` parameters for each dimension.
    :return:       Regularly distributed rectangular mesh grid.
    """
    linspaces = [numpy.linspace(a, b, num=n)
                 for (a, b), n in zip(ranges, shape)]
    return numpy.meshgrid(*linspaces)


def meshgrid_ranges(grid):
    """
    Returns ranges, enclosing given `grid`.
    This ranges effectively are just minimum and maximum values along each of
    grid axes.

    :param grid: N-dimensional `numpy` meshgrid.
    :return: List of tuples, where each tuple is a lower and upper bounds for
             corresponding axis of the grid.

    Example:

        >>> import numpy
        >>> grid = numpy.meshgrid(numpy.linspace(0, 1),
        ...                       numpy.linspace(2, 3),
        ...                       numpy.linspace(4, 5))
        >>> meshgrid_ranges(grid)
        [(0.0, 1.0), (2.0, 3.0), (4.0, 5.0)]

    """
    return [(numpy.min(axis), numpy.max(axis)) for axis in grid]


def adjust_uniform_random(array, a, b):
    a, b = sorted([a, b])
    array /= (b - a)
    array -= a