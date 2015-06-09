import itertools
import glob
import re
import numpy
from rvlm.labhelpers.trivia import omit_empty_items

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

def filter_by_key(data, pattern, keytype=float):
    """
    """
    pattern = re.escape(pattern)
    pattern = pattern.replace(re.escape("{}"), "([\\d.Ee+-]+)")
    phi_rex = re.compile(pattern)

    def extractKey(name):
        try:
            m = phi_rex.match(name)
            return float(m.group(1))
        except:
            return None

    result = {}
    for name, value in data.items():
        key = keytype(extractKey(name))
        if key is not None:
            result[key] = value

    return result
