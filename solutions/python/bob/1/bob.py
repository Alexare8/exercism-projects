def response(hey_bob):
    msg = hey_bob.strip()
    if msg == "":
        return "Fine. Be that way!"
    if msg.isupper() and msg[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if msg.isupper():
        return "Whoa, chill out!"
    if msg[-1] == "?":
        return "Sure."
    return "Whatever."