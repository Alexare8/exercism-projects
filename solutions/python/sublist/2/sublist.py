"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = 1
SUBLIST = 2
SUPERLIST = 3
UNEQUAL = 4


def sublist(list_one: list[int], list_two: list[int]) -> int:
    """Determines list_one's relationship to list_two, coded as an int.
        EQUAL = 1
        SUBLIST = 2
        SUPERLIST = 3
        UNEQUAL = 4
    """
    if list_one == list_two:
        return EQUAL
    len_one = len(list_one)
    len_two = len(list_two)
    if len_one < len_two:
        if any(list_one == list_two[i:i + len_one] for i in range(len_two - len_one + 1)):
            return SUBLIST
    if len_one > len_two:
        if any(list_two == list_one[i:i + len_two] for i in range(len_one - len_two + 1)):
            return SUPERLIST
    return UNEQUAL