from math import isqrt


def prime(number: int) -> int:
    """Retrns the Nth prime number."""
    if number == 0:
        raise ValueError('there is no zeroth prime')
    primes = []
    checking = 1
    while len(primes) < number:
        checking += 1
        if is_prime(checking):
            primes.append(checking)
    return checking


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