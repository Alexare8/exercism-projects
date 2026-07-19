import re
import operator
QUESTION_RE = re.compile(r"(?:What|Who) is ([a-zA-Z0-9-+*/ ]+)\?")
OPS_DICT = {"plus": "+", "minus": "-", "multiplied by": "*", "divided by": "/"}
OPS_FUNC_DICT = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
MATH_RE = re.compile(r"[0-9-+*/ ]+")


def answer(question: str) -> int:
    """Validates and evaluates a math word problem."""

    # Part 1, Initial Validation
    if (match := re.fullmatch(QUESTION_RE, question)):
        problem = match.group(1)
    else:
        raise ValueError("syntax error")
    
    # Part 2, Parse into Arithmetic
    for name, symbol in OPS_DICT.items():
        problem = problem.replace(name, symbol)
    if not (match := re.fullmatch(MATH_RE, problem)):
        raise ValueError("unknown operation")
    problem = problem.split()
    problem = list(reversed(problem))

    # Part 3, Calculation
    if problem[-1] in "+-*/":
        raise ValueError("syntax error")
    result = int(problem.pop())
    while problem != []:
        if len(problem) < 2 or problem[-2] in "+-*/" or problem[-1].isdigit():
            raise ValueError("syntax error")
        result = OPS_FUNC_DICT[problem.pop()](result, int(problem.pop()))
    return int(result)
        
