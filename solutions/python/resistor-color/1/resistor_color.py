resistor_colors = ["black", "brown", "red", "orange", "yellow" ,"green", "blue", "violet", "grey", "white"]


def color_code(color: str) -> int:
    return resistor_colors.index(color)


def colors() -> list:
    return  resistor_colors
