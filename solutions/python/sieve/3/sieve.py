def primes(limit: int) -> list[int]:
    """Find primes up to the given number using the Sieve of Eratosthenes"""
    unseen = [True for _ in range(0, limit + 1)]
    prime_list = []
    for number in range(2, limit + 1):
        if unseen[number] is True:
            prime_list.append(number)
            next_num = number * 2
            while limit >= next_num:
                unseen[next_num] = False
                next_num += number
    return prime_list
