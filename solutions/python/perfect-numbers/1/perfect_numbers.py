from math import sqrt, floor

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: raise ValueError("Classification is only possible for positive integers.")
    sum = aliquot(number)
    if sum < number:
        return "deficient"
    if sum > number:
        return "abundant"
    return "perfect"


def aliquot(number):
    """ Returns the aliquot sum of an integer, the sum of each of it's factors, not including itself.

    :param number: int a positive integer
    :return: int aliquot sum of number
    """
    if number < 1: raise ValueError("Classification is only possible for positive integers.")

    factors = set(factor for factor in range(floor(sqrt(number)), number) if number % factor == 0)
    factors = factors.union([number//factor for factor in factors])
    factors = factors.union([1]).difference([number])
    return sum(factors)
    