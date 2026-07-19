from collections.abc import Iterable


def flatten(iterable: list) -> list:
    """Flatten arbitrarily nested list, with the items in the same order, removing any None."""
    flat = []
    for item in iterable:
        if item is None:
            continue
        if isinstance(item, Iterable):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
