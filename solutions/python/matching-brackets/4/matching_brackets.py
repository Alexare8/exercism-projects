PAIRS = {")": "(", "]": "[", "}": "{"}


def is_paired(input_string: str) -> bool:
    """Checks if all pairs of brackets are nested properly."""
    cleaned = "".join(char for char in input_string if char in "()[]{}")
    stack = []

    for char in cleaned:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            previous = stack.pop()
            if previous == PAIRS[char]:
                continue
            return False
            
    return not stack