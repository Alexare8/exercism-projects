class Luhn:
    def __init__(self, card_num):
        self.number = card_num

    def valid(self):
        if len(self.number.replace(" ", "")) < 2 or not (clean_number := self.number.replace(" ", "")).isdigit():
            return False
        doubled_digits = sum(doubled if (doubled := int(digit) * 2) < 10 else doubled - 9 for digit in clean_number[-2::-2])
        other_digits = sum(int(n) for n in clean_number[-1::-2])
        return (doubled_digits + other_digits) % 10 == 0
