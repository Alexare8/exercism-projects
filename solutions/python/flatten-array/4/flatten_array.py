from collections.abc import Iterable


def flatten(iterable: list) -> list:
    """Accepts arbitrarily nested lists and returns one flat list, with the items in the same order, removing any None"""
    flat = []
    for item in iterable:
        if item == None:
            continue
        if isinstance(item, Iterable):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
