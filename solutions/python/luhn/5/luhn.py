from itertools import cycle
from operator import call


class Luhn:
    def __init__(self, card_num):
        self.number = card_num.replace(" ", "")

    def valid(self):
        if len(self.number) < 2 or not self.number.isdigit():
            return False
        modified = map(call, cycle((lambda x: x, normalize)), map(int, reversed(self.number)))
        return sum(modified) % 10 == 0


def normalize(n: int) -> int:
    n *= 2
    while n > 9: n -= 9
    return n
