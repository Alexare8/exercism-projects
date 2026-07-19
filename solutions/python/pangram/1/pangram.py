def is_pangram(sentence):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if not letter in sentence.lower():
            return False
    return True
