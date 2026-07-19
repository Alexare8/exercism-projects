def is_paired(input_string: str) -> bool:
    """Checks if all pairs of brackets are nested properly."""

    cleaned = "".join(char for char in input_string if char in "()[]{}")
    for _ in range(len(cleaned)):

        # Quick tests for end before doing the loop
        if cleaned == "":
            return True
        if cleaned[0] in ")]}" or cleaned[-1] in "([{":
            return False
        
        # Not done yet, remove the next pair
        for i, char in enumerate(cleaned):
            if char not in ")]}":
                continue
            if (char == ")" and cleaned[i - 1] == "(") or (char == "]" and cleaned[i - 1] == "[") or (char == "}" and cleaned[i - 1] == "{"):
                cleaned = cleaned[:i - 1] + cleaned[i + 1:]
                break
            return False

    return True
