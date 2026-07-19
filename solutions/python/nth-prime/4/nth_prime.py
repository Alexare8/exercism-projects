from itertools import islice, count
from math import isqrt


def prime(number: int) -> int:
    """Returns the Nth prime number."""
    if number == 0:
        raise ValueError('there is no zeroth prime')
    return list(islice(filter(is_prime, count(2)), number)).pop()


def is_prime(n: int) -> bool:
    """Returns True if input is a prime number."""
    return all((n % i != 0) for i in range(2, isqrt(n)))
