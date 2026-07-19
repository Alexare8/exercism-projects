ops_dict = {"plus": "+", "minus": "-", "multiplied by": "*", "divided by": "/"}


def answer(question: str) -> int:
    expression = question[:-1]
    for op in ops_dict.items():
        expression = expression.replace(*op)
    expression = expression.split()
    if expression.pop(0) + expression.pop(0) != "Whatis":
        raise ValueError("unknown operation")
    
    print(list(expression))
    #TODO: loop through expression and validate each term? or something? 


print(answer("What is -3 multiplied by 25?"))
print(answer("What is 5?"))
print(answer("What is 17 minus 6 plus 3?"))
print(answer("What is 123 plus 45678?"))