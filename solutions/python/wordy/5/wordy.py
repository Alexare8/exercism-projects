import re
QUESTION_RE = re.compile(r"(?:What|Who) is ([a-zA-Z0-9-+*/ ]+)?")
MATH_RE = re.compile(r"[0-9-+*/ ]+")
OPS_DICT = {"plus": "+", "minus": "-", "multiplied by": "*", "divided by": "/"}


def answer(question: str) -> int:
    """Validates and evaluates a math word problem."""

    # Part 1, Initial Validation
    match = re.match(QUESTION_RE, question)
    if (match := re.match(QUESTION_RE, question)):
        problem = match.group(1)
    else:
        raise ValueError("syntax error")
    
    # Part 2, Parse into Arithmetic
    for name, symbol in OPS_DICT.items():
        problem = problem.replace(name, symbol)
    if not (match := re.match(MATH_RE, problem)):
        raise ValueError("unknown operation")
    problem = problem.split()
    
    # Part 3, Calculation 
    # TODO: Make it work, make it not use eval()
    result = problem.pop()
    while problem != []:
        if len(problem) < 2 or not problem[-1] in "+-*/" or not (problem[-2].isdigit() or "-" in problem[-2]):
            raise ValueError("syntax error")
        result = eval(f"{result}{problem.pop()}{problem.pop()}")
    return int(result)
        
