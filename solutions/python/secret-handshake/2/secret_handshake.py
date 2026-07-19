def commands(binary: str) -> list[str]:
    """Decode the given binary number into the correct secret handshake"""
    MOVES = ["wink", "double blink", "close your eyes", "jump"]
    handshake = [move for move, bit in zip(MOVES, binary[-1:0:-1]) if bit == "1"]
    if binary[0] == "1":
        handshake.reverse()
    return handshake
