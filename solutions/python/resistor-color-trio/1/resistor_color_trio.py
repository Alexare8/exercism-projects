COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]


def label(colors) -> str:
    """Decode a resistor's color bands to return it's resistance (tolerance ignored)"""
    value = (10 * COLORS.index(colors[0]) + COLORS.index(colors[1])) * (10 ** COLORS.index(colors[2]))
    prefix = 0
    while value % 1000 == 0 and value != 0:
        value = value // 1000
        prefix += 1
    return f"{value} {['', 'kilo', 'mega', 'giga'][prefix]}ohms"
