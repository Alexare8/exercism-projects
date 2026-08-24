def encode(numbers: list[int]) -> list[int]:
    """Encode a list if numbers as a list of variable length quantity bytes."""
    bytes_: list[int] = []
    for number in numbers:
        bytes_.extend(number_to_vlq(number))
    return bytes_


def decode(bytes_: list[int]) -> list[int]:
    """Decode a list of variable length quantity bytes into a list of numbers."""
    numbers: list[int] = []
    vlq: list[int] = []
    open_sequence = False
    for byte in bytes_:
        vlq.append(byte)
        open_sequence = True
        if byte < 128:
            numbers.append(vlq_to_number(vlq))
            vlq = []
            open_sequence = False

    if open_sequence:
        raise ValueError("incomplete sequence")

    return numbers


def number_to_vlq(number: int) -> list[int]:
    """Encode a number into a variable length quantity."""
    if number == 0:
        return [0]

    bytes_: list[int] = []
    mask = (1 << 7) - 1
    while number > 0:
        bytes_.append(number & mask)
        number = number >> 7

    bytes_.reverse()
    for i, part in enumerate(bytes_[:-1]):
        bytes_[i] = part + 128

    return bytes_


def vlq_to_number(bytes_: list[int]) -> int:
    """Decode a variable length quantity."""
    if len(bytes_) == 1:
        return bytes_[0]

    number = 0
    for byte in bytes_[:-1]:
        byte_value = byte - 128
        number = (number << 7) | byte_value

    number = (number << 7) | bytes_[-1]
    return number
