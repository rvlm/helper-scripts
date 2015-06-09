
def omit_empty_items(sequence):
    """
    Filters out sequence entries which are :const:`None` or empty. If argument
    is :const:`None` than the return value is :const:`None` too, but if argument
    is empty an empty sequence, another empty sequence is returned.
    """
    if sequence is None:
        return None
    else:
        return filter(lambda x: x (is not None) and (len(x) != 0), sequence)
