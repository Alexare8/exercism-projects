def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a number as a list of digits from the input base to the output base"""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not digits or all(digit == 0 for digit in digits):
        return [0]

    return decimal_to_base(output_base, base_to_decimal(input_base, digits))


def base_to_decimal(input_base: int, digits: list[int]) -> int:
    """Convert a number as a list of digits in the input base into a decimal integer"""
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * input_base + digit
    return decimal_value


def decimal_to_base(output_base: int, number: int) -> list[int]:
    """Convert a decimal integer to a number as a list of digits in the ouput base"""
    digits: list[int] = []
    while number != 0:
        number, remainder = divmod(number, output_base)
        digits.append(remainder)
    return list(reversed(digits))
