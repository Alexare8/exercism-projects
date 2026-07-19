OPS_DICT = {"plus": "+", "minus": "-", "multiplied": "*", "divided": "/"}


def answer(question: str) -> int:
    """Validates and evaluates a math word problem."""

    problem = question[8:-1].split()
    problem = problem[::-1]
    if problem == []:
        raise ValueError("syntax error")
    while "by" in problem:
        problem.remove("by")
    for i, term in enumerate(problem):
        print("Inside for loop, term:", term)
        if term in OPS_DICT:
            print(f"Replacing {term} with {OPS_DICT[term]}")
            problem[i] = OPS_DICT[term]
        elif not (term.isdigit() or "-" in term):
            raise ValueError("unknown operation")
    print("done with for loop",problem)
    result = problem.pop()
    while problem != []:
        if len(problem) < 2 or not problem[-1] in "+-*/" or not (problem[-2].isdigit() or "-" in problem[-2]):
            raise ValueError("syntax error")
        result = eval(f"{result}{problem.pop()}{problem.pop()}")
    return int(result)
        