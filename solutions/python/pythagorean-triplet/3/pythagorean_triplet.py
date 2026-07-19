from math import sqrt, gcd


def triplets_with_sum(number: int) -> list[list]:
    """Find all pythagorean triplets that total a given sum."""
    triplets = []
    for m in range(2, int(sqrt(number)) + 1):
        for n in range(1, m):
            if gcd(m,n) == 1 and (m-n) % 2 == 1 and m * m + n * n < number:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                for k in range(0, number // c + 1):
                    if k * a + k * b + k * c == number:
                        triplets.append(sorted([k * a, k * b, k * c]))
    return triplets