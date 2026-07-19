def primes(limit: int) -> list[int]:
    """Find primes up to the given number using the Sieve of Eratosthenes"""
    unseen = [True for _ in range(0, limit + 1)]
    prime_list = []
    for number in range(2, limit + 1):
        if unseen[number]:
            prime_list.append(number)
            for i in range(number, limit + 1, number):
                unseen[i] = False
    return prime_list
