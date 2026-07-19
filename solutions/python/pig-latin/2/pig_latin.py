import re

def translate(text):
    # Seperate into words, translate individually, then recombine
    return " ".join((pig_latin(word) for word in text.split(" ")))


def pig_latin(word):
    # Determine what needs to be moved, and separate it into 'start'
    start, end = re.findall(r"(^[^aeiou]*q?u?)([aeiouy]+.*$)", word)[0]
    # If there's a start to move, move it
    if start != "" and start[:2] != "xr" and start[:2] != "yt":
        return end + start + "ay"
    return word + "ay"