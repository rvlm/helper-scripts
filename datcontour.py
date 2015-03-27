#!/usr/bin/env python
import os
import sys
import numpy
import svgwrite
from rvlm.entrypoint import mainfunction

paper_formats_mm = {
    "A3": (297, 420),
    "A4": (210, 297),
    "A5": (148, 210),
}

@mainfunction()
def main(inputFile, outputFile, profile=True, fill=True,
                landscape=True, units = "mm", paper="A4"):
    """
    Draws data contour into SVG file for futher processing and printing. This
    was originally indended as planar antennas manufacturing step.

    :param inputFile:  Data file with space separated X-Y values.
    :param outputFile: File to write drawing into.
    :param profile:    Automatically close antenna profile.
    :param fill:       Fill contour with black color.
    :param landscape:  Use landscape paper orientation.
    :param units:      X and Y units: mm (default), cm
    :param paper:      Paper size (case sensitive): A5, A4 (default), A3
    """
    data = None
    with open(inputFile, mode="r") as ifile:
        data = numpy.loadtxt(ifile, usecols=(0, 1))

    if profile:
        x0 = data[0,0]
        x1 = data[-1,0]
        data = numpy.vstack(([x0, 0], data, [x1, 0]))

    if units == "mm":
        pass
    elif units == "cm":
        data *= 10
    else:
        sys.stderr.write("Unsupported unit name, must be either 'mm' or 'cm'.\n")
        sys.exit(os.ERR_FAIL)
        
    size = paper_formats_mm.get(paper, None)
    if size is None:
        sys.stderr.write("Unsupported paper format.\n")
        sys.exit(os.ERR_FAIL)
        
    if not landscape:
        (wx, wy) = size
    else:
        (wy, wx) = size

    size = ("%dmm" % wx, "%dmm" % wy)
    vBox = "0 0 %d %d" % (wx, wy)
    
    dwg  = svgwrite.Drawing(filename=outputFile, size=size, viewBox=vBox)
    poly = dwg.polygon(data, stroke="black", stroke_width = 0.1, fill = "black" if fill else "none")

    dwg.add(poly)
    dwg.save()
