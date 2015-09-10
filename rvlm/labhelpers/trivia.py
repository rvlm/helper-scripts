
def omit_empty_items(sequence):
    """
    Filters out sequence entries which are :const:`None` or empty. If argument
    is :const:`None` than the return value is :const:`None` too, but if argument
    is empty an empty sequence, another empty sequence is returned.
    """
    if sequence is None:
        return None
    else:
        return filter(lambda x: (x is not None) and (len(x) != 0), sequence)

def tuple1(lst):
    """
    Converts list to tuple or single value. If argument :param:`lst` is a list
    (or other enumerable) holding more than one item, then this function
    returns a tuple with the same values with their original order preserved.
    If argument hold only single value, that value itself is returned.
    """
    ts = tuple(lst)
    if len(ts) == 0: return None
    if len(ts) == 1: return ts[0]
    return ts

def head(lst):
    """
    """
    try:
        return iter(lst).next()
    except StopIteration:
        return None

def applyfs(fs, args):
    return map(lambda f: f(*args), fs)

def unpackf(f):
    return (lambda args: f(*args))
