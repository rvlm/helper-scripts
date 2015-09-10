"""
"""
import numpy
from functools                   import partial
from rvlm.labhelpers.extdict     import mapv
from rvlm.labhelpers.timesignals import signal_energy


def energy_pattern(signals_dict, normalize=False, equidistant=False):
    """
    Calculates antenna energy pattern from a bunch of signals emitted into
    different directions. This function takes a dictionary where keys are
    direction angles, values are signals, emitting to that direction.
    """
    result = mapv(partial(signal_energy, equidistant=equidistant), signals_dict)
    result = numpy.array(sorted(result.items()))

    if normalize:
        result[:,1] /= numpy.max(numpy.abs(result[:,1]))

    return result
