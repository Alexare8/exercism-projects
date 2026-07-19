def append(list1: list, list2: list) -> list:
    """Given two lists, add all items in the second list to the end of the first list"""
    both = list1
    for item in list2:
        both.append(item)
    return both


def concat(lists: list[list]) -> list:
    """given a series of lists, combine all items in all lists into one flattened list"""
    accum = []
    for a_list in lists:
        for item in a_list:
            accum.append(item)
    return accum


def filter(function, list: list) -> list:
    """given a predicate and a list, return the list of all items for which `predicate(item)` is True"""
    filtered = []
    for item in list:
        if function(item):
            filtered.append(item)
    return filtered


def length(list: list) -> int:
    """given a list, return the total number of items within it"""
    return sum(1 for item in list)


def map(function, list: list) -> list:
    """given a function and a list, return the list of the results of applying `function(item)` on all items"""
    return [function(item) for item in list]


def foldl(function, list: list, initial):
    """given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left"""
    accum = initial
    for item in list:
        accum = function(accum, item)
    return accum


def foldr(function, list: list, initial):
    """given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the right"""
    accum = initial
    for item in list[::-1]:
        accum = function(accum, item)
    return accum


def reverse(list: list) -> list:
    """given a list, return a list with all the original items, but in reversed order"""
    return list[::-1]