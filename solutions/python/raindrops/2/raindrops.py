LOOKUP = {3: "Pling", 5: "Plang", 7: "Plong"}


def convert(number):
    message = "".join(word for factor, word in LOOKUP.items() if number % factor == 0)
    if not message:
        return str(number)
    return message
    
