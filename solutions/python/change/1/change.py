from functools import cache


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target == 0:
        return []
    if target < 0:
        raise ValueError("target can't be negative")
    if all(target < coin for coin in coins):
        raise ValueError("can't make target with given coins")

    sorted_coins = sorted(coins, reverse=True)

    @cache
    def find_coins(target: int) -> list[int]:
        if all(target < coin for coin in sorted_coins):
            return [-1]
        potential_change: list[list[int]] = []
        for coin in sorted_coins:
            if target == coin:
                return [coin]
            if target > coin:
                result = find_coins(target - coin)
                if result != [-1]:
                    potential_change.append([coin] + result)

        if not potential_change:
            return [-1]
        return min(potential_change, key=len)

    shortest_change = find_coins(target)

    if shortest_change == [-1]:
        raise ValueError("can't make target with given coins")

    return sorted(shortest_change)
