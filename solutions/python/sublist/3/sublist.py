# Possible sublist categories.
# Change the values as you see fit.
EQUAL = 1
SUBLIST = 2
SUPERLIST = 3
UNEQUAL = 4


def sublist(list_one: list, list_two: list) -> int:
    """Return list_one's relationship to list_two, coded as an int.

        EQUAL = 1
        SUBLIST = 2
        SUPERLIST = 3
        UNEQUAL = 4
    """
    if list_one == list_two:
        return EQUAL
    if isSublist(list_one, list_two):
        return SUBLIST
    if isSublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

def isSublist(list_one: list, list_two: list) -> bool:
    return any(list_one == list_two[i:i + len(list_one)] for i in range(len(list_two) - len(list_one) + 1))