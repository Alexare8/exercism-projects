from typing import Generator


def factors(value: int) -> list[int]:
    """Return a list of the input's prime factors."""
    prime_factors = []
    remaining = value
    prime_numbers = primes(value)
    for prime in prime_numbers:
        while value % prime == 0:
            value //= prime
            prime_factors.append(prime)
    return prime_factors
    

def primes(n: int) -> Generator[int, None, None]:
    """Generates primes with the Sieve of Eratosthenes, at 1,000,000"""
    if n == 2 or n == 3:
        yield n
    else:
        if n > 1_000_000:
            n = 1_000_000
        sieve = [True] * (n+1)
        for p in range(2,n+1):
            if sieve[p]:
                for i in range(p*p, n, p):
                    sieve[i] = False
            yield p

    