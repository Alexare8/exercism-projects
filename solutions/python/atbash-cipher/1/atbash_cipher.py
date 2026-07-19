def encode(plain_text: str) -> str:
    """Encode a string with the atbash cipher."""
    message = plain_text.replace(" ", "").lower()
    message = "".join(chr(219 - ord(char)) if char.isalpha() else char for char in message if char.isalnum())
    chunks = []
    while message != "":
        if len(message) > 5:
            chunks.append(message[:5])
            message = message[5:]
        else:
            chunks.append(message[:])
            message = ""
    return " ".join(chunks)

def decode(ciphered_text: str) -> str:
    """Decode atbash cipher text"""
    return str("".join(chr(219 - ord(char)) if char.isalpha() else char for char in ciphered_text if char != " "))
