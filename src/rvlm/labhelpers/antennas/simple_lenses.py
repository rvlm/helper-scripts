import math
import numpy
import rvlm.labhelpers.extnumpy as extnumpy

def spherical_wavefront_lense(eps0, R, angle, num, realistic=True, omit_outer_points=True):
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
    def epsilon(x,y,z):
        result = eps0 * z*z / (x*x + y*y)
        if realistic and result < 1.0:
            result = 1.0

        return result
            
    grid = numpy.meshgrid(numpy.linspace(-R, R, num=num),
                          numpy.linspace(-R, R, num=num),
                          numpy.linspace( 0, R, num=num))

    result = extnumpy.tabularf(grid, [f])

    if omit_outer_points:
        pred = lambda (x,y,z,_): abs(x*x + y*y)/(z*z) < math.tan(angle)**2
        result = extnumpy.filter_along_axis(pred, 1, result)

    return result
    
