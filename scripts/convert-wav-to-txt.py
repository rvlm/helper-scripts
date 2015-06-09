#!/usr/bin/env python2
import wave
import math
import numpy
import sys

if len(sys.argv) < 3:
    print "Usage: %s INPUT OUTPUT" % sys.argv[0]
    sys.exit(1);

ifile = sys.argv[1];
ofile = sys.argv[2];

types = {
    1: numpy.int8,
    2: numpy.int16,
    4: numpy.int32
}

wav = wave.open(ifile, mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

content = wav.readframes(nframes)
samples = numpy.fromstring(content, dtype=types[sampwidth])

channel = 0
samples = samples[channel::nchannels]

with open(ofile, mode="w") as f:
    for sample in samples:
        f.write("%d\n" % sample)

