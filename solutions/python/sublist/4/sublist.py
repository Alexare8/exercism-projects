import typing

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = 1
SUBLIST = 2
SUPERLIST = 3
UNEQUAL = 4


def sublist(list_one: list[typing.Any], list_two: list[typing.Any]) -> int:
    """Return list_one's relationship to list_two, coded as an int.

        EQUAL = 1
        SUBLIST = 2
        SUPERLIST = 3
        UNEQUAL = 4
    """
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def is_sublist(list_one: list[typing.Any], list_two: list[typing.Any]) -> bool:
    return any(
        list_one == list_two[i:i + len(list_one)]
        for i in range(len(list_two) - len(list_one) + 1)
    )
