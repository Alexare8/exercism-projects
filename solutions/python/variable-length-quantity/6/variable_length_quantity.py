CONTINUATION_BIT = 0x80  # 0b10000000
DATA_MASK = 0x7F  # 0b01111111


def encode(numbers: list[int]) -> list[int]:
    """Encode a list of numbers as a list of variable length quantity bytes."""
    bytes_: list[int] = []
    for number in numbers:
        bytes_.extend(number_to_vlq(number))
    return bytes_


def decode(bytes_: list[int]) -> list[int]:
    """Decode a list of variable length quantity bytes into a list of numbers."""
    numbers: list[int] = []
    number = 0
    open_sequence = False
    for byte in bytes_:
        number = (number << 7) | (byte & DATA_MASK)
        open_sequence = bool(byte & CONTINUATION_BIT)
        if not open_sequence:
            numbers.append(number)
            number = 0

    if open_sequence:
        raise ValueError("incomplete sequence")

    return numbers


def number_to_vlq(number: int) -> list[int]:
    """Encode a number into a variable length quantity."""
    if number == 0:
        return [0]

    bytes_: list[int] = []
    while number > 0:
        bytes_.append(number & DATA_MASK)
        number >>= 7

    bytes_.reverse()
    for i, byte in enumerate(bytes_[:-1]):
        bytes_[i] = byte | CONTINUATION_BIT

    return bytes_
