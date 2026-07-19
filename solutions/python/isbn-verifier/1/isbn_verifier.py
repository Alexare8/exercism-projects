def is_valid(isbn: str) -> bool:
    number = isbn.replace("-", "")
    if number[:-1].isdigit() and len(number) == 10:
        number, check_sum = number[:-1], number[-1]
        if not check_sum.isdigit():
            if check_sum == "X":
                check_sum = 10
            else:
                return False
        check_sum = 11 - int(check_sum)
        return sum(i * int(digit) for i, digit
                   in zip(range(10, 1, -1), number)) % 11 == check_sum
    return False
    