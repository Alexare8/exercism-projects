import re

pattern = re.compile(r"What is (-?\d+(?!\d))? ?([\+\-\*/](?!\d))? ?(-?\d+(?!\d))? ?([\+\-\*/](?!\d))? ?(-?\d+(?!\d))")
ops_dict = {"plus": "+", "minus": "-", "multiplied by": "*", "divided by": "/"}


# Regex was not the right course for this one. This iteraion fails 3 tests.
def answer(question: str) -> int:
    """Answer a mathematical word question."""
    parsed = question
    for op in ops_dict.items():
        parsed = parsed.replace(*op)
    result = pattern.search(parsed)
    if not result:
        raise ValueError("unknown operation")
    expression = [term for term in result.groups() if term]
    print(expression)
    if len(expression) == 2 or len(expression) == 4:
        raise ValueError("syntax error")
    if len(expression) == 1 or len(expression) == 3:
        if len(expression) == 3 and expression[1] not in "+-*/":
            raise ValueError("syntax error")
        return eval("".join(expression))
    if len(expression) == 5:
        return eval("({}{}{}){}{}".format(*expression))
    