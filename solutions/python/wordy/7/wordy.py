from itertools import batched
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

    # Part 3, Calculation
    try:
        result = int(problem.pop(0))
        for operator, operand in batched(problem, 2):
            result = OPS_FUNC_DICT[operator](result, int(operand))
        return int(result)
    except:
        raise ValueError("syntax error")
        