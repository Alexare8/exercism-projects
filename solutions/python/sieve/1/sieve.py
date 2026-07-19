def primes(limit: int) -> list[int]:
    """Find primes up to the given number using the Sieve of Eratosthenes"""
    numbers = list(range(2, limit+1))
    prime_list = []
    while numbers:
        new_prime = numbers.pop(0)
        prime_list.append(new_prime)
        next = new_prime * 2
        while limit >= next:
            if next in numbers:
                numbers.remove(next)
            next += new_prime
    return prime_list
