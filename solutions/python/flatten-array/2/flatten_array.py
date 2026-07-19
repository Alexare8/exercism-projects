from collections.abc import Iterable


def flatten(iterable):
    flat = []
    change = False
    for item in iterable:
        if item == None:
            continue
        if isinstance(item, Iterable):
            flat.extend(item)
            change = True
        else:
            flat.append(item)
    if change:
        return flatten(flat)
    return flat
