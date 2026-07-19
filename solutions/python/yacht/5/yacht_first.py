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
        case ONES|TWOS|THREES|FOURS|FIVES|SIXES:
            return dice.count(category) * category
        case CHOICE:
            return sum(dice)
        case FULL_HOUSE:
            if ((dice.count(dice[0]) == 3 and dice.count(dice[-1]) == 2) or
                (dice.count(dice[0]) == 2 and dice.count(dice[-1]) == 3)):
                return sum(dice)
        case FOUR_OF_A_KIND:
            if dice.count(dice[2]) >= 4:
                return dice[2] * 4
        case LITTLE_STRAIGHT:
            if dice == set(1, 2, 3, 4, 5):
                return 30
        case BIG_STRAIGHT:
            if dice == set(2, 3, 4, 5, 6):
                return 30
        case YACHT:
            if dice.count(dice[0]) == 5:
                return 50        
    
    return 0
