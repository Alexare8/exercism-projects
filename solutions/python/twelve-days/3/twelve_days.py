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
LINE_START = "On the {} day of Christmas my true love gave to me: "
                #{DAYS[verse]}

def recite(start_verse: int, end_verse: int) -> list[str]:
    """Returns verses of the song 'The Twelve Days of Christmas'"""
    return [LINE_START.format(DAYS[verse]) + "".join(GIFTS[i] for i in range(verse, 0, -1))
            for verse in range(start_verse, end_verse + 1)]
