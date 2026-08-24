def encode(numbers: list[int]) -> list[int]:
    """Encode a list if numbers as a list of variable length quantity bytes."""
    bytes: list[int] = []
    for number in numbers:
        bytes.extend(number_to_vlq(number))
    return bytes


def decode(bytes: list[int]) -> list[int]:
    """Decode a list of variable length quantity bytes into a list of numbers."""
    numbers: list[int] = []
    vlq: list[int] = []
    open_sequence = False
    for byte in bytes:
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

    bytes: list[int] = []
    mask = (1 << 7) - 1
    while number > 0:
        bytes.append(number & mask)
        number = number >> 7

    bytes.reverse()
    for i, part in enumerate(bytes[:-1]):
        bytes[i] = part + 128

    return bytes


def vlq_to_number(bytes: list[int]) -> int:
    """Decode a variable length quantity."""
    if len(bytes) == 1:
        return bytes[0]

    number = 0
    for byte in bytes[:-1]:
        byte = byte - 128
        number = (number << 7) | byte

    number = (number << 7) | bytes[-1]
    return number
