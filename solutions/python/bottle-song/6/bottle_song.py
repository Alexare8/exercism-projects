VERSE_FORM = (
    "{} hanging on the wall,", 
    "{} hanging on the wall,", 
    "And if one green bottle should accidentally fall,", 
    "There'll be {} hanging on the wall."
)
BOTTLE_COUNTS = (
    "no green bottles",
    "one green bottle",
    "two green bottles",
    "three green bottles",
    "four green bottles",
    "five green bottles",
    "six green bottles",
    "seven green bottles",
    "eight green bottles",
    "nine green bottles",
    "ten green bottles"
)


def recite(start: int, take: int = 1) -> list[str]:
    """Recite requested verses of the song 'Ten Green Bottles'"""
    return [line for i in range(start, start - take, -1) for line in verse(i) + [""]][:-1]


def verse(number: int) -> list[str]:
    """Assemble a verse of 'Ten Green Bottles'"""
    count = BOTTLE_COUNTS[number].capitalize()
    next_count = BOTTLE_COUNTS[number - 1]
    return [
        VERSE_FORM[0].format(count),
        VERSE_FORM[1].format(count),
        VERSE_FORM[2],
        VERSE_FORM[3].format(next_count)
    ]
