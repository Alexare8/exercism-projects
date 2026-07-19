DIGIT_NAMES = {0: "",1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
               17: "seventeen", 18: "eighteen", 19: "nineteen"}
TENS_NAMES = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def say(number: int) -> str:
    """Returns the english reading of the given positive integer."""
    if number < 0 or number >= 1e12:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    digits = str(number).rjust(12, "0")
    print(digits)
    thousand, million, billion = "", "", ""
    one = triplet(int(digits[9:]))
    if number >= 1e3:
        thousand = triplet(int(digits[6:9]))
        if thousand:
            thousand += " thousand"
    if number >= 1e6:
        million = triplet(int(digits[3:6]))
        if million:
            million += " million"
    if number >= 1e9:
        billion = triplet(int(digits[0:3]))
        if billion:
            billion += " billion"
    
    return f"{billion} {million} {thousand} {one}".strip()



"nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three"

def triplet(number: int) -> str:
    "Returns the english reading of a three digit long segment of a number."
    print("in triplet:", number)
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

    if (hundred := number // 100) == 0:
        hundred = ""
    else:
        hundred = DIGIT_NAMES[hundred] + " hundred "
    return f"{hundred}{tens}{ones}"


#while True:
#    print(say(input("Number: ")))
    