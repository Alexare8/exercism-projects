def append(list1: list, list2: list) -> list:
    """Add all items in the second list to the end of the first list."""
    return list1 + list2    # Does this couont as not "using existing functions"?
                            # This is called 'append' here but it behaves like Python's 'extend'
                            # If I'm not supposed to use the '+' operator, my only other option afaik is
                            # to use 'append' and that seems more against the spirit of the exercise.


def concat(lists: list[list]) -> list:
    """Combine all items in all lists into one flattened list."""
    return [item for a_list in lists for item in a_list]


def filter(function, list: list) -> list:
    """Test each item in list with function, return list of items that returned True."""
    return [item for item in list if function(item)]


def length(list: list) -> int:
    """Return number of items in a list."""
    return sum(1 for item in list)


def map(function, list: list) -> list:
    """Apply function to each item in list, return list of results."""
    return [function(item) for item in list]


def foldl(function, list: list, initial):
    """Reduce each item into an accumulator from the left."""
    accum = initial
    for item in list:
        accum = function(accum, item)
    return accum


def foldr(function, list: list, initial):
    """Reduce each item into an accumulator from the right."""
    accum = initial
    for item in list[::-1]:
        accum = function(accum, item)
    return accum


def reverse(list: list) -> list:
    """Reverse the order of a list."""
    return list[::-1]