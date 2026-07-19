def is_isogram(string):
    chars = list(string.lower().replace(" ", "").replace("-", ""))
    return len(set(chars)) == len(chars)


print(is_isogram("-n-nmia"))
