# Score categories.
# Change the values as you see fit.
YACHT = 'yacht'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'full house'
FOUR_OF_A_KIND = 'four of a kind'
LITTLE_STRAIGHT = 'little straight'
BIG_STRAIGHT = 'big straight'
CHOICE = 'choice'


def score(dice: list[int], category: int | str):
    """Calculate the score of a Yacht roll"""
    dice = sorted(dice)
    match category:
        case 1|2|3|4|5|6:
            return dice.count(category) * category
        case 'choice':
            return sum(dice)
        case 'full house':
            if ((dice.count(dice[0]) == 3 and dice.count(dice[-1]) == 2) or
                (dice.count(dice[0]) == 2 and dice.count(dice[-1]) == 3)):
                return sum(dice)
        case 'four of a kind':
            if dice.count(dice[2]) >= 4:
                return dice[2] * 4
        case 'little straight':
            if dice == set(1, 2, 3, 4, 5):
                return 30
        case 'big straight':
            if dice == set(2, 3, 4, 5, 6):
                return 30
        case 'yacht':
            if dice.count(dice[0]) == 5:
                return 50        
    
    return 0
