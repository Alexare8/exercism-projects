import re
atternpay = re.compile(r"(^qu|^q|^[^aeiouq]+(?:qu)?)(?=[aeiouy])")
# new pattern, it's kind of a beast

def translate(text):
    # Seperate into words, translate individually, then recombine
    return " ".join(pig_latin(word) for word in text.split())


def pig_latin(word):
    match = re.match(atternpay, word)
    if match and "xr" not in match.group() and "yt" not in match.group():
        word = word[len(match.group()):] + match.group()
        # would word.replace(match.group(), "") be better?
    return word + "ay"


# yeah okay naming varibles in pig latin
# isn't best practice but it made me smile