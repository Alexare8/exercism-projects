from random import sample
from string import ascii_uppercase, digits


class Robot:

    named_robots = []

    def __init__(self):
        self.reset()


    def reset(self):
        self.name = self.name_gen()
        Robot.named_robots.append(self.name)


    def name_gen(self):
        name = ""
        while name in Robot.named_robots or name == "":
            name = "".join(sample(ascii_uppercase, 2) + sample(digits, 3))
        return name