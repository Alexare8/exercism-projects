from math import isqrt


def prime(number: int) -> int:
    """Returns the Nth prime number."""
    if number == 0:
        raise ValueError('there is no zeroth prime')
    primes = []
    checking = 1
    while len(primes) < number:
        checking += 1
        if all_prime(checking):
            primes.append(checking)
    return checking


def all_prime(n: int) -> bool:
    """Returns True if input is a prime number."""
    return all((n % i != 0) for i in range(2, n))


def is_prime(n: int) -> bool: 
    """Returns True if input is a prime number."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True