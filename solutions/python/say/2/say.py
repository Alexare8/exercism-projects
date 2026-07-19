DIGIT_NAMES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS_NAMES = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
MAG_NAMES = ["billion", "million", "thousand", ""]


def say(number: int) -> str:
    """Returns the english reading of the given positive integer."""
    if number < 0 or number >= 1e12:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    digits = str(number).rjust(12, "0")
    sections = " ".join(list(part for i, name in enumerate(MAG_NAMES) if (part := triplet(int(digits[i*3: i*3 + 3]), name))))
    return sections


def triplet(number: int, magnitude: str) -> str:
    "Returns the english reading of a segment of a number with it's magnitude."
    if number == 0:
        return ""
    
    ones = DIGIT_NAMES[number % 10]
    if (tens := number % 100) == 0:
        tens = ""
    elif tens < 20:
        tens = DIGIT_NAMES[tens]
        ones = ""
    else:
        tens = TENS_NAMES[tens // 10]
        if ones:
            tens += "-"
    if (hundreds := number // 100) == 0:
        hundreds = ""
    else:
        hundreds = DIGIT_NAMES[hundreds] + " hundred "

    number = (hundreds + tens + ones).strip()
    if magnitude:
        number += " " + magnitude
    return number
