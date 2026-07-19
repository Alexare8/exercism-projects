VERSE_FORM = [
    "{} hanging on the wall,", 
    "{} hanging on the wall,", 
    "And if one green bottle should accidentally fall,", 
    "There'll be {} hanging on the wall."
]
BOTTLE_COUNTS = {
    0: "no green bottles",
    1: "one green bottle",
    2: "two green bottles",
    3: "three green bottles",
    4: "four green bottles",
    5: "five green bottles",
    6: "six green bottles",
    7: "seven green bottles",
    8: "eight green bottles",
    9: "nine green bottles",
    10: "ten green bottles"
}


def recite(start: int, take: int = 1) -> list[str]:
    """Recite requested verses of the song 'Ten Green Bottles'"""
    song: list[str] = []
    for i in range(start, start - take, -1):
        if song:
            song.append("")
        song.extend(verse(i))
    return song


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