from typing import Generator
from math import isqrt


def factors(value: int) -> list[int]:
    """Return a list of the input's prime factors."""
    prime_factors = []
    prime_numbers = primes(value)
    for prime in prime_numbers:
        print(f"Main loop, checking if {value} is multiple of {prime}")
        while value % prime == 0:
            value //= prime
            prime_factors.append(prime)
    return prime_factors
    

def primes(n: int) -> Generator[int, None, None]:
    """Generates primes with the Sieve of Eratosthenes, capped at 1,000,000."""
    print(f"In primes(), n is {n}")
    for i in range(n+1):
        if is_prime(i):
            yield i


def is_prime(n: int) -> bool:
    """Returns True if input is a prime number."""
    print(f"In is_prime(), n is {n}")
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True
