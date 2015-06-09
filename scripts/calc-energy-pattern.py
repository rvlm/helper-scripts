#!/usr/bin/env python
import re
import numpy
import itertools
from rvlm.entrypoint import mainfunction

def non_empty(lst):
    return filter(lambda x: x != "", lst)
    
def read_cst_ascii(stream):
    header_rex = re.compile('\\s\\s+')

    result = {}
    try:
        iterator = iter(stream)
        while True:
            section = itertools.takewhile(lambda s: s.strip() != "",  iterator)
            header = section.next()
            (xhdr, yhdr) = non_empty(header_rex.split(header))

            sepline = section.next()
            sepline = sepline.strip()
            if not all(map(lambda ch: ch == '-', sepline)):
                break

            result[yhdr] = numpy.loadtxt(section)

    except StopIteration:
        pass

    return result
            

@mainfunction()
def main(pattern, inputFile, outputFile, normalize=True):
    probes = None
    with open(inputFile, mode="r") as f:
        probes = read_cst_ascii(f)

    pattern = re.escape(pattern)
    pattern = pattern.replace("\\@", "([\\d.Ee+-]+)")
    phi_rex = re.compile(pattern)
        
    def extractArgument(name):
        try:
            m = phi_rex.match(name)
            return float(m.group(1))
        except:
            return None
            

    def extractTheta(s):
        pass

    def calculateEnergy(signal):
        result = 0
        for v in signal[:,1]:
            result += v*v

        return result

    result = {}
    for name, signal in probes.items():
        arg = extractArgument(name)
        if arg is not None:
            print signal
            result[arg] = calculateEnergy(signal)

    print result
    result = numpy.array(sorted(result.items()))
    numpy.savetxt(outputFile, result)
