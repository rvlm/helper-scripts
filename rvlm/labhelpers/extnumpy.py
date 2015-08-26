import numpy

def tabularf(axes, funcs = []):
    """
    Produces list of points for an N-dimentional mesh grid. This table can also
    be extended with values of arbitrary functions computed on the points. For
    example:

        >>> import numpy
        >>> import operator
        >>> xspace = numpy.linspace(0, 1, num=2)
        >>> yspace = numpy.linspace(2, 3, num=2)
        >>> [xs, ys] = numpy.meshgrid(xspace, yspace)
        >>> extnumpy.tabularf([xs, ys])
        array([[ 0.,  2.],
               [ 1.,  2.],
               [ 0.,  3.],
               [ 1.,  3.]])

        >>> extnumpy.tabularf([xs, ys], [operator.add, operator.mul])
        array([[ 0.,  2.,  2.,  0.],
               [ 1.,  2.,  3.,  2.],
               [ 0.,  3.,  3.,  0.],
               [ 1.,  3.,  4.,  3.]])

    This method is especially useful for saving multidimentional data in a form
    readable by a human. Use :func:`numpy.savetxt` for actual saving to file.
    """
    def appendf(args):
        fvals = [f(*args) for f in funcs]
        return list(args) + fvals

    baxes = numpy.array(list(numpy.broadcast(*axes)))
    return numpy.apply_along_axis(appendf, 1, baxes)

