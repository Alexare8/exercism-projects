def primes(limit: int) -> list[int]:
    """Find primes up to the given number using the Sieve of Eratosthenes"""
    numbers = list(range(limit, 1, -1))
    prime_list = []
    while numbers:
        new_prime = numbers.pop()
        prime_list.append(new_prime)
        next_num = new_prime * 2
        while limit >= next_num:
            if next_num in numbers:
                numbers.remove(next_num)
            next_num += new_prime
    return prime_list
