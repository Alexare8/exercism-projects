COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]
TOLERANCES = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%",
              "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%"}


def resistor_label(colors: list[str]) -> str:
    """Decode a resistor's color bands to return it's resistance and tolerance"""
    if colors == ["black"]:
        return "0 ohms"
    tolerance, multiplier = TOLERANCES[colors.pop()], COLORS.index(colors.pop())
    value = (10 * COLORS.index(colors[0]) + COLORS.index(colors[1]))
    if len(colors) == 3:
        value = value * 10 + COLORS.index(colors[2])
    value *= 10 ** multiplier
    value, prefix = metric_prefix(value)
    return f"{value} {prefix}ohms ±{tolerance}"


def metric_prefix(number: int) -> tuple[float, str]:
    """Divides input by increments of 1000 and returns the new value and appropriate metric prefix"""
    prefix = 0
    while number > 1000:
        number /=  1000
        prefix += 1
    if number % 1 == 0:
        number = int(number)
    return number, ["", "kilo", "mega", "giga"][prefix]