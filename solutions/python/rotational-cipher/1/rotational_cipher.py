def rotate(text: str, key: int):
    if not 0 <= key <= 26:
        raise ValueError("Key must be an int from 0 to 26, inclusive")
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = alphabet[key:] + alphabet[:key]
    cipher = {**dict(zip(alphabet, cipher)), **dict(zip(alphabet.upper(), cipher.upper()))}

    return "".join(cipher[char] if char in cipher else char for char in list(text))
