import re


def decode(string: str) -> str:
    """Decode a run-length encoded string."""
    output = ""
    
    if matches := re.findall(r"(\d*[a-z\s])", string, flags=re.I):
        for match in matches:
            if len(match) == 1:
                output += match
            else:
                output += match[-1] * int(match[:-1])

    return output


def encode(string: str) -> str:
    """Encode a string with run-length encoding."""
    output = ""
    collect = ""

    for letter in string:
        if letter not in collect and len(collect) != 0:
            if len(collect) > 1:
                output += f"{len(collect)}"
            output += f"{collect[0]}"
            collect = ""
        collect += letter

    if len(collect) != 0:
        if len(collect) > 1:
            output += f"{len(collect)}"
        output += f"{collect[0]}"

    return output
