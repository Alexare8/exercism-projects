from random import sample
from string import ascii_uppercase, digits


class Robot:

    named_robots = []

    def __init__(self):
        self.name = self.name_gen()
        Robot.named_robots.append(self.name)


    def reset(self):
        self.__init__()


    def name_gen(self):
        name = "".join(sample(ascii_uppercase, 2) + sample(digits, 3))
        while name in Robot.named_robots:
            name = "".join(sample(ascii_uppercase, 2) + sample(digits, 3))
        return name