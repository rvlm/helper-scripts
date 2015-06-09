#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import re
import argparse
import locale
import operator
import numpy
from matplotlib import axis
from matplotlib import rc, rcParams
from matplotlib import pyplot as plt


# Hash of global parameters shared between different option handlers,
# with default values.
params = {
    "format"   : "png",
    "encoding" : "utf-8",
    "mirror"   : False }


# Unfortunately, Python syntax disallows assignments in lambdas. So, instead
# of lambda: params[key] = val one have to write lambda: setparam(key, val).
def setparam(name, val):
    params[name] = val


# Decodes string from local encoding to unicode where local encoding is
# specified with '--encoding' switch and is UTF-8 by default.
def decode(s):
    return unicode(s, encoding=params['encoding'])


def readFile(filename, cols):
    # Thanks to http://stackoverflow.com/a/4703508/1447225.
    rex_pattern = r"""
        [-+]?                  # optional sign
        (?: (?: \d* \. \d+ ) | # .1 .12 .123 etc 9.1 etc 98.1 etc
            (?: \d+ \.? ))     # 1. 12. 123. etc 1 12 123 etc
        (?: [Ee] [+-]? \d+ )?  # followed by optional exponent part if desired """
    rex = re.compile(rex_pattern, re.VERBOSE)

    result = []
    with open(filename, mode="r") as f:
        for line in f:
            vals = map(float, rex.findall(line))
            if len(vals) >= 2:
                result.append(tuple(vals))

    return numpy.array(result)

def mirror(dat):
    a = dat.copy()
    a[:,0] *= -1
    a = numpy.vstack((a, dat))
    return numpy.array(sorted(a, key=operator.itemgetter(0)))


def addhandler(parser, name, nargs=None, type=None, handler=None):
    class PlotAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            handler(*values)

    # Note that 'PlotAction' class is local to 'add' function and gets
    # redefined every time it's called.
    parser.add_argument(name, nargs=nargs, type=type, action=PlotAction)


def plot(f, cols):
    dat = readFile(f, cols)
    if params["mirror"]:
        dat = mirror(dat)

    plt.plot(dat[:,0], dat[:,1])

def xcaption(s):
    tickpad  = rcParams['xtick.major.pad']
    fontsize = rcParams['font.size']
    plt.annotate(s, xy=(1,0), xytext=(0, -tickpad - fontsize),
        ha='center',
        va='top',
        xycoords='axes fraction',
        textcoords='offset points')


def ycaption(s):
    tickpad  = rcParams['ytick.major.pad']
    fontsize = rcParams['font.size']
    plt.annotate(s, xy=(0,1), xytext=(-tickpad, (fontsize + tickpad)/2),
        ha='center',
        va='bottom',
        xycoords='axes fraction',
        textcoords='offset points')


# Available command line options, their parameter and handlers.
# This is the list of tuples (name, nargs, type, handler).
options = [
    ("eval",        1, None,     lambda v:   eval(v)),
    ("format",      1, None,     lambda v:   setparam("format", v)),
    ("encoding",    1, None,     lambda v:   setparam("encoding", v)),
    ("mirror",      1, bool,     lambda v:   setparam("mirror", v)),
    ("line-color",  1, None,     lambda v:   rc("lines", color=v)),
    ("line-width",  1, None,     lambda v:   rc("lines", width=v)),
    ("line-style",  1, None,     lambda v:   rc("lines", style=v)),
    ("marker",      1, None,     lambda v:   rc("lines", marker=v)),
    ("markersize",  1, None,     lambda v:   rc("lines", markersize=v)),
    ("font-family", 1, None,     lambda v:   rc("font",  family=v)),
    ("font-weight", 1, None,     lambda v:   rc("font",  weigth=v)),
    ("font-size",   1, float,    lambda v:   rc("font",  size=v)),
    ("dpi",         1, float,    lambda d:   rc("savefig", dpi=d)),
    ("figsize",     2, float,    lambda x,y: plt.figure(figsize=(x,y))),
    ("grid",        1, bool,     lambda v:   plt.grid(v)),
    ("xlabel",      1, None,     lambda v:   plt.xlabel(decode(v))),
    ("ylabel",      1, None,     lambda v:   plt.ylabel(decode(v))),
    ("xlim",        2, float,    lambda a,b: plt.xlim(a,b)),
    ("ylim",        2, float,    lambda a,b: plt.ylim(a,b)),
    ("ylog",        1, bool,     lambda v:   plt.yscale('log')),
    ("xcaption",    1, None,     lambda v:   xcaption(decode(v))),
    ("ycaption",    1, None,     lambda v:   ycaption(decode(v))),
    ("plot",        1, None,     lambda f:   plot(decode(f)))]


# --- main ---
locale.setlocale(locale.LC_ALL, "")
rc("axes.formatter", use_locale=True)

parser = argparse.ArgumentParser()
for (dest, nargs, argtype, handler) in options:
    addhandler(parser, "--%s" % dest, nargs, argtype, handler)

parser.add_argument("outfile")
parser.add_argument("files", nargs='*')

result = parser.parse_args()
for f in result.files:
    plot(decode(f), (0, 1))

plt.savefig(result.outfile, format=params['format'])
