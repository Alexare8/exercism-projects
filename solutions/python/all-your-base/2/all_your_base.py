from math import floor, log


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a number as a list of digits from the input base to the output base"""
    if not input_base >= 2:
        raise ValueError("input base must be >= 2")
    if not output_base >= 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if digits == [] or all(digit == 0 for digit in digits):
        return [0]

    return decimal_to_base(output_base, base_to_decimal(input_base, digits))


def base_to_decimal(input_base: int, digits: list[int]) -> int:
    """Convert a number as a list of digits in the input base into a decimal integer"""
    digit_values = []
    for power, digit in enumerate(reversed(digits)):
        print(f"({input_base} ** {power}) * {digit} = {input_base**power * digit}")
        digit_values.append(input_base**power * digit)
    return sum(digit_values)


def decimal_to_base(output_base: int, number: int) -> list[int]:
    """Convert a decimal integer to a number as a list of digits in the ouput base"""
    remainder = number
    digits = []
    highest_power = floor(log(number, output_base))
    for power in range(highest_power, -1, -1):
        print(
            f"({remainder} // {output_base}) ** {power} = {remainder // output_base**power}"
        )
        digits.append(remainder // output_base**power)
        remainder = remainder % output_base**power
    return digits
