import numpy

def timesignal(sequence):
    return numpy.vstack( (numpy.arange(len(sequence)), sequence ))

def normalize(sig):
    sig[:,1] /= numpy.max(numpy.abs(sig[:,1]))

def normalized(sig):
    sig = sig.copy()
    normalize(sig)
    return sig

def argmin(sig):
    return sig[numpy.argmin(sig[:, 1]), 0]

def argmax(sig):
    return sig[numpy.argmax(sig[:, 1]), 0]

def signal_max_shift(reference, signal):
    """
    """
    return argmax(signal) - argmax(reference)
