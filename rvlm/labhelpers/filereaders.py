import itertools
import glob
import re
import numpy
from rvlm.labhelpers.trivia import omit_empty_items, tuple1

def read_agilent_waveform(stream):
    """
    """
    try:
        iterator = iter(stream)
        iterator = itertools.dropwhile(lambda s: s.strip() != "Data,", iterator)
        iterator.next()
        return numpy.loadtxt(iterator, delimiter=", ")
    except StopIteration:
        return None

def read_cst_ascii(stream):
    """
    """
    header_rex = re.compile('\\s\\s+')
    result = {}
    try:
        iterator = iter(stream)
        while True:
            section = itertools.takewhile(lambda s: s.strip() != "",  iterator)
            header = section.next()
            (xhdr, yhdr) = omit_empty_items(header_rex.split(header))

            sepline = section.next()
            sepline = sepline.strip()
            if not all(map(lambda ch: ch == '-', sepline)):
                break

            result[yhdr] = numpy.loadtxt(section)

    except StopIteration:
        pass

    return result

def read_files(filename_pattern, reader=numpy.loadtxt):
    """
    """
    result = {}
    for filename in glob.iglob(filename_pattern):
        with open(filename, mode="r") as f:
            result[filename] = reader(f)

    return result
