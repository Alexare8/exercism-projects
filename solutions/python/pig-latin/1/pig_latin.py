import re

def translate(text):
    return " ".join((pig_latin(word) for word in text.split(" ")))


def pig_latin(word):
    start, end = re.findall(r"(^[^aeiou]*q?u?)([aeiouy]+.*$)", word)[0]        
    if start != "" and start[:2] != "xr" and start[:2] != "yt":
        return end + start + "ay"
    return word + "ay"