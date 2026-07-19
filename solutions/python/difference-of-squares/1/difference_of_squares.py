def square_of_sum(number: int) -> int:
    """Return square of sum of natural numbers up to given number"""
    total = (number * (number + 1) // 2)
    return total ** 2

def sum_of_squares(number: int) -> int:
    """Return sum of squares of natural numbers up to given number"""
    return number * (number + 1) * (2 * number + 1) / 6


def difference_of_squares(number: int) -> int:
    """Returns the difference between the square of the sum, and the sum of the squares,
        of natural numbers up to given number"""
    return (number - 1) * number * (number + 1) * (3 * number + 2) / 12