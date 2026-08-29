from collections import deque


def encode(message: str, rails: int) -> str:
    """Encode a message with the Rail Fence Cipher"""
    message_rails: list[list[str]] = [[] for _ in range(rails)]
    rail = 0
    increment = 1
    for char in message:
        message_rails[rail].append(char)
        if rail == 0 and increment == -1 or rail == rails - 1 and increment == 1:
            increment *= -1
        rail += increment

    return "".join("".join(message_rail) for message_rail in message_rails)


def decode(encoded_message: str, rails: int) -> str:
    """Decode a message encoded with the Rail Fence Cipher"""
    # calculate length of rails
    period = 2 * (rails - 1)
    rail_lengths: list[int] = []
    for i in range(rails):
        base_length, remainder = divmod(len(encoded_message), period)
        if i in {0, rails - 1}:
            length = base_length
            length += remainder > i
        else:
            length = base_length * 2
            length += remainder > i
            length += remainder - rails > rails - 1 - i
        rail_lengths.append(length)

    # break encoded message into rails
    message_rails: list[deque[str]] = []
    consumed = 0
    for rail, length in enumerate(rail_lengths):
        message_rails.append(deque(encoded_message[consumed : consumed + length]))
        consumed += length

    # assemble decoded message from rails
    decoded_message: list[str] = []
    rail = 0
    increment = -1
    for i in range(len(encoded_message)):
        decoded_message.append(message_rails[rail].popleft())
        if rail == 0 and increment == -1 or rail == rails - 1 and increment == 1:
            increment *= -1
        rail += increment

    return "".join(decoded_message)


def rail_length(message: str, rails: int) -> list[int]:
    """Utility to figure out what the rail length should be for a given message length"""
    message_rails: list[list[str]] = [[] for _ in range(rails)]
    rail = 0
    increment = 1
    for char in message:
        message_rails[rail].append(char)
        if rail == 0 and increment == -1 or rail == rails - 1 and increment == 1:
            increment *= -1
        rail += increment

    return [len(rail) for rail in message_rails]
