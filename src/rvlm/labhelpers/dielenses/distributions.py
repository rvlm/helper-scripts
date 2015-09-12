import math
import numpy
from rvlm.labhelpers.tabular  import tabularmf
from rvlm.labhelpers.extnumpy import filter_along_axis


def spherical_wavefront_lens(eps0, R, angle, num,
                             realistic=True, omit_outer_points=True):
    """
    Generates a table describing the distribution of epsilon (material
    permittivity) in space in order to compensate spherically curved wavefront
    in a conic antenna.

    :param eps0:
    :param R:
    :param angle:
    :param num:
    :param realistic:
    :param omit_outer_points:
    """
    def epsilon(x, y, z):
        result = eps0 * z*z / (x*x + y*y)
        if realistic and result < 1.0:
            result = 1.0

        return result

    grid = numpy.meshgrid(numpy.linspace(-R, R, num=num),
                          numpy.linspace(-R, R, num=num),
                          numpy.linspace( 0, R, num=num))

    result = tabularmf(grid, [epsilon])
    if omit_outer_points:
        cutoff = lambda (x,y,z,_): abs(x*x + y*y)/(z*z) < math.tan(angle)**2
        result = filter_along_axis(cutoff, 1, result)

    return result
