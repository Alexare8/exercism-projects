def answer(question: str) -> int:
    """Validates and evaluates a math word problem."""
    problem = question[8:-1].split()
    while "by" in problem:
        problem.remove("by")
    print(problem)

    if len(problem) == 1:
        return int(problem[0])
    if len(problem) in (3, 5):
        if problem[1] not in ["plus", "minus", "multiplied", "divided"]:
            raise ValueError("unknown operation")
        if not problem[0].isalpha() and problem[1].isalpha() and not problem[2].isalpha():
            
            if problem[1] == "plus":
                result = int(problem[0]) + int(problem[2])
            elif problem[1] == "minus":
                result = int(problem[0]) - int(problem[2])
            elif problem[1] == "multiplied":
                result = int(problem[0]) * int(problem[2])
            elif problem[1] == "divided":
                result = int(problem[0]) // int(problem[2])
            else:
                raise ValueError("unknown operation")
    else:
        raise ValueError("syntax error")
    
    if len(problem) == 5:
        if problem[3] not in ["plus", "minus", "multiplied", "divided"]:
            raise ValueError("unknown operation")
        if problem[3].isalpha() and not problem[4].isalpha():
            if problem[3] == "plus":
                result = result + int(problem[4])
            elif problem[3] == "minus":
                result = result - int(problem[4])
            elif problem[3] == "multiplied":
                result = result * int(problem[4])
            elif problem[3] == "divided":
                result = result // int(problem[4])
            else:
                raise ValueError("unknown operation")
        else:
            raise ValueError("syntax error")


    return result