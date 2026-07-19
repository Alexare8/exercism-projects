# Score categories.
# Change the values as you see fit.
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full house'
FOUR_OF_A_KIND = 'four of a kind'
LITTLE_STRAIGHT = 'little straight'
BIG_STRAIGHT = 'big straight'
CHOICE = 'choice'


def score(dice, category):
    dice = sorted(dice)
    match category:
        case 'ones':
            return dice.count(1)
        case 'twos':
            return dice.count(2) * 2
        case 'threes':
            return dice.count(3) * 3
        case 'fours':
            return dice.count(4) * 4
        case 'fives':
            return dice.count(5) * 5
        case 'sixes':
            return dice.count(6) * 6
        case 'choice':
            return sum(dice)
        
        case 'full house':
            if ((dice.count(dice[0]) == 3 and dice.count(dice[-1]) == 2) or
                (dice.count(dice[0]) == 2 and dice.count(dice[-1]) == 3)):
                return sum(dice)
        case 'four of a kind':
            if dice.count(dice[0]) >= 4:
                return dice[0] * 4
            elif dice.count(dice[-1]) >= 4:
                return dice[-1] * 4
        case 'little straight':
            if sorted(dice) == [1, 2, 3, 4, 5]:
                return 30
        case 'big straight':
            if sorted(dice) == [2, 3, 4, 5, 6]:
                return 30
        case 'yacht':
            if dice.count(dice[0]) == 5:
                return 50        
    
    return 0