from itertools import islice, count


def prime(number: int) -> int:
    """Returns the Nth prime number."""
    if number == 0:
        raise ValueError('there is no zeroth prime')
    primes = prime_gen()
    for _ in range(number):
        out = next(primes)
    return out


def prime_gen() -> int:
    """Generates prime numbers in order."""
    prime_numbers = []
    integers = count(2)
    for i in integers:
        if all(i % prime != 0 for prime in prime_numbers):
            prime_numbers.append(i)
            yield(i)
