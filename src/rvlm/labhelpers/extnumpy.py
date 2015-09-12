"""

"""
import numpy


def hstack_skip_empty(*arrays):
    """
    """
    return numpy.hstack(tuple(filter(lambda a: a.size > 0, arrays)))


def vstack_skip_empty(*arrays):
    """
    """
    return numpy.vstack(tuple(filter(lambda a: a.size > 0, arrays)))


def filter_along_axis(pred, axis, array):
    """ http://stackoverflow.com/a/26154854/1447225
    """
    bool_array = numpy.apply_along_axis(pred, axis, array)
    return array[bool_array]
