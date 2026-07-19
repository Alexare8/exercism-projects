from itertools import count
from math import isqrt


def prime(number: int) -> int:
    """Returns the Nth prime number."""
    if number == 0:
        raise ValueError('there is no zeroth prime')
    primes = filter(is_prime, count(2))
    for _ in range(number - 1):
        next(primes)
    return next(primes)


def is_prime(n: int) -> bool:
    """Returns True if input is a prime number."""
    return all((n % i != 0) for i in range(2, isqrt(n) + 1))
