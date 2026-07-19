from random import randint


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self) -> int:
        return sum(sorted(randint(1, 6) for _ in range(4))[1:])

def modifier(number: int) -> int:
    return (number - 10) // 2