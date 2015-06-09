#!/usr/bin/env python2
import wave
import math
import numpy
import sys

if len(sys.argv) < 4:
    print "Usage: %s FREQ SCALE INPUT OUTPUT" % sys.argv[0]
    sys.exit(1);

freq = int(sys.argv[1])
scale = float(sys.argv[2])
ifile = sys.argv[3]
ofile = sys.argv[4]

samples = []
with open(ifile, mode="r") as f:
    samples = [int(scale*float(s)) for s in f]
    samples = numpy.array(samples, dtype=numpy.int16)

w = wave.open(ofile, mode="w")
w.setparams( (1, 2, freq, 0, "NONE", "NONE") )
w.writeframes(samples.tostring())
w.close()

