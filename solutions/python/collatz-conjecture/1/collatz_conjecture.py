def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    temp = number
    count = 0
    while temp != 1:
        count += 1
        temp = collatz_step(temp)
    return count

    
def collatz_step(number):
    if number % 2 == 0:
        return number / 2
    return 3 * number + 1