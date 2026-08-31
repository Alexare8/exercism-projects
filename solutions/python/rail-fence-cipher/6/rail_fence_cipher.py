from collections import Counter, deque


def encode(message: str, rails: int) -> str:
    """Encode a message with the Rail Fence Cipher"""
    message_rails: list[list[str]] = [[] for _ in range(rails)]
    rail = 0
    increment = 1
    for char in message:
        message_rails[rail].append(char)
        if (rail == 0 and increment == -1) or (rail == rails - 1 and increment == 1):
            increment *= -1
        rail += increment

    return "".join("".join(message_rail) for message_rail in message_rails)


def decode(encoded_message: str, rails: int) -> str:
    """Decode a message encoded with the Rail Fence Cipher"""
    zigzag_rails: list[int] = []
    rail = 0
    increment = 1
    for _ in encoded_message:
        zigzag_rails.append(rail)
        if (rail == 0 and increment == -1) or (rail == rails - 1 and increment == 1):
            increment *= -1
        rail += increment

    rail_lengths = Counter(zigzag_rails)

    message_rails: list[deque[str]] = []
    consumed = 0
    for rail_index in range(rails):
        length = rail_lengths[rail_index]
        message_rails.append(deque(encoded_message[consumed : consumed + length]))
        consumed += length

    decoded_message: list[str] = []
    for rail_index in zigzag_rails:
        decoded_message.append(message_rails[rail_index].popleft())

    return "".join(decoded_message)
