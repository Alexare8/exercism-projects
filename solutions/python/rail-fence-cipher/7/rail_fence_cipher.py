from collections import Counter, deque


def encode(message: str, rails: int) -> str:
    """Encode a message with the Rail Fence Cipher."""
    message_rails: list[list[str]] = [[] for _ in range(rails)]
    rail_pattern = create_rail_pattern(rails, len(message))

    for char_index, char in enumerate(message):
        message_rails[rail_pattern[char_index]].append(char)

    return "".join("".join(message_rail) for message_rail in message_rails)


def decode(encoded_message: str, rails: int) -> str:
    """Decode a message encoded with the Rail Fence Cipher."""
    rail_pattern = create_rail_pattern(rails, len(encoded_message))
    rail_lengths = Counter(rail_pattern)

    message_rails: list[deque[str]] = []
    consumed = 0
    for rail_index in range(rails):
        length = rail_lengths[rail_index]
        message_rails.append(deque(encoded_message[consumed : consumed + length]))
        consumed += length

    decoded_message: list[str] = []
    for rail_index in rail_pattern:
        decoded_message.append(message_rails[rail_index].popleft())

    return "".join(decoded_message)


def create_rail_pattern(rails: int, message_length: int) -> list[int]:
    """Determine which rail each character in a message of given length will end up on."""
    if rails == 1:
        return [0 for _ in range(message_length)]
    rail_pattern: list[int] = []
    rail = 0
    increment = 1
    for _ in range(message_length):
        rail_pattern.append(rail)
        if (rail == 0 and increment == -1) or (rail == rails - 1 and increment == 1):
            increment *= -1
        rail += increment

    return rail_pattern
