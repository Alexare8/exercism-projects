from random import sample


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
        return sum(sorted(roll_dice(4, 6))[1:])


def modifier(abil_score: int) -> int:
    return (abil_score - 10) // 2

def roll_dice(num_dice: int, num_sides: int) -> list[int]:
    return sample(range(1, num_sides + 1), num_dice)