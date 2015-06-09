import numpy

def signal_energy(signal, equidistant=False):
    """
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

def energy_pattern(sighash, normalize=False, equidistant=False):
    """
    """
    result = {}
    for k, sig in sighash.items():
        result[k] = signal_energy(sig, equidistant=equidistant)

    result = numpy.array(sorted(result.items()))

    if normalize:
        result[:,1] /= numpy.max(numpy.abs(result[:,1]))

    return result
