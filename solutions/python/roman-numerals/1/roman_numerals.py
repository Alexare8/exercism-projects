NUMERAL_LOOKUP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def roman(number: int) -> str:
    """Returns the given value as a roman numeral."""    
    first_pass = ""
    roman_numeral = ""
    for numeral, value in NUMERAL_LOOKUP.items():
        while number >= value:
            number -= value
            first_pass += numeral
            
    for i, numeral in enumerate(NUMERAL_LOOKUP.keys()):
        if first_pass.count(numeral) == 4:
            if list(NUMERAL_LOOKUP.keys())[i - 1] in first_pass:
                roman_numeral = f"{roman_numeral[:-1]}{numeral}{list(NUMERAL_LOOKUP.keys())[i - 2]}"
            else:
                roman_numeral += f"{numeral}{list(NUMERAL_LOOKUP.keys())[i - 1]}"
        else:
            roman_numeral += numeral * first_pass.count(numeral)
    return roman_numeral
