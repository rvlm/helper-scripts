"""

"""
import numpy


def timesignal(sequence):
    return numpy.vstack( (numpy.arange(len(sequence)), sequence ))


def normalize(signal):
    """
    Scales `signal` to fit into the [-1...1] range of values. Specifically,
    this is achieved by dividing all signal samples by signal maximum absolute
    value.

    This function performs its operation in-place, effectively modifying
    original array.
    """
    signal[:,1] /= numpy.max(numpy.abs(signal[:,1]))


def normalized(signal):
    """
    Returns a normalized copy of `signal`.
    """
    signal = signal.copy()
    normalize(signal)
    return signal


def argmin(signal):
    return signal[numpy.argmin(signal[:, 1]), 0]


def argmax(signal):
    return signal[numpy.argmax(signal[:, 1]), 0]


def signal_max_shift(reference, signal):
    """
    """
    return argmax(signal) - argmax(reference)


def signal_energy(signal, equidistant=False):
    """
    Calculates total energy of the `signal`. This value is computed according
    to the following integral:

    .. math:: \int\limits_{-\infty}^{infty} s(t)^2 dt \approx
              \sum\limits_{i=0}^{N} s_i^2 dt_i

    If the signal is sampled at regular intervals, setting option `equidistant`
    to `True` would result to a faster computation.
    """
    if equidistant:
        result = 0
        dt = signal[0,0] - signal[1,0]
        for v in signal[:,1]:
            result += v*v

        return result
    else:
        result = 0
        tprev = signal[0,0]
        vprev = signal[0,1]**2
        for t, v in signal[1:]:
            result += (vprev + v**2)/2.0 * (t-tprev)

        return result