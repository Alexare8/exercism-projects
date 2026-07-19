import re
pattern = re.compile(r"^(qu|q|[^aeiouq]+(?:qu)?)(?=[aeiouy])")
# new pattern, it's kind of a beast

def translate(text):
    # Seperate into words, translate individually, then recombine
    return " ".join(pig_latin(word) for word in text.split())


def pig_latin(word):
    match = re.match(pattern, word)
    if match and "xr" not in match.group() and "yt" not in match.group():
        word = word[len(match.group()):] + match.group()
    return word + "ay"
    