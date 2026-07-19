NUMERAL_LOOKUP = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400,
    "C": 100, "XC": 90, "L": 50, "XL": 40, 
    "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
    }


def roman(number: int) -> str:
    """Returns the given value as a roman numeral."""    
    roman_numeral = ""
    for numeral, value in NUMERAL_LOOKUP.items():
        while number >= value:
            number -= value
            roman_numeral += numeral
    return roman_numeral
