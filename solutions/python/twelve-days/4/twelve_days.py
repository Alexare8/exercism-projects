GIFTS = [
    "",
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, and ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]
DAYS = [
    "", "first", "second", "third", "fourth",
    "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth"
]

def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return a range of verses of the song 'The Twelve Days of Christmas'"""
    return [verse(verse_number) for verse_number in range(start_verse, end_verse + 1)]

def verse(verse:int) -> str:
    """Assenble a verse of 'The Twelve Days of Christmas'"""
    return (f"On the {DAYS[verse]} day of Christmas my true love gave to me: " +
            "".join(GIFTS[i] for i in range(verse, 0, -1)))