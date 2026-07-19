def is_armstrong_number(number):
    digits = list(str(number))
    return number == sum((int(n) ** len(digits) for n in digits))
        
        