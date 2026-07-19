def find(search_list: list[int], value: int) -> int:
    """Use binary search to return the given item's index in the given list."""
    if len(search_list) == 0:
        raise ValueError("value not in array")
    if len(search_list) == 1:
        return 0
    
    left, right, middle = 0, len(search_list) - 1, len(search_list) // 2
    for _ in range(right):
        if value < search_list[left] or value > search_list[right] or left > right:
            raise ValueError("value not in array")
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            right = middle -1
            middle //= 2
        else:
            left = middle + 1
            middle = (left + right) // 2

