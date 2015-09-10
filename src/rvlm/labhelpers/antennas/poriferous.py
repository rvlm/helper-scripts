"""
xxx
"""
import functools
import operator
import numpy
from scipy.optimize import leastsq

def holeBox(r, deltas, holePos, holeWidths):
    """
    xxx
    """
    
    def intersection(aMin, aMax, bMin, bMax):
        """
        xxx
        """
        assert(aMin <= aMax)
        assert(bMin <= bMax)

        aLen = aMax - aMin
        bLen = bMax - bMin
        if aLen > bLen:
            return intersection(bMin, bMax, aMin, aMax)

        if aMin < bMin and aMax > bMin: return aMax - bMin
        if aMin < bMax and aMax > bMax: return bMax - aMin
        if aMin > bMin and aMax < bMax: return aLen
        return 0
    
    result = 1.0
    for x, d, p, w in zip(r, deltas, holePos, holeWidth):
        result *= intersection(x-d/2.0, x+d/2.0, p-w/2.0, p+w/2.0)

    return result

def synthesizeConstantsHoles(epsilon, backEpsilon, ranges, deltas,
                      holesCount, holeFunction, holeParams):
    """
    :param epsilon:
    :param backEpsilon:
    :param ranges:
    :param deltas:
    :param holesCount:
    :param holeFunction:
    :param holeParams:
    """
    assert(epsilon.ndim == len(ranges))
    assert(epsilon.ndim == len(deltas))

    mult = numpy.product(deltas)

    def gridCoordinates(array, ranges):
        linspaces = [numpy.linspace(a, b, n)
                     for (a, b), n in zip(ranges, array.shape)]
        return numpy.meshgrid(*linspaces)
    
    def target(params):
        grid = gridCoordinates(epsilon, ranges)
        hf = [holeFunction(r, deltas, params, holeParams) for r in grid]
        vs = numpy.sum(hf, axis=0)
        return epsilon - backEpsilon + 1/mult * vs

    p0
    plsq = leastsq(target, p0)

