def commands(binary_str: str) -> list[str]:
    """Decode the given binary string into the correct secret handshake"""
    binary = int(binary_str, 2)
    MOVES = ["wink", "double blink", "close your eyes", "jump"]
    handshake = [move for index, move in enumerate(MOVES) if binary & (1 << index)]
    if binary & 16:
        handshake.reverse()
    return handshake