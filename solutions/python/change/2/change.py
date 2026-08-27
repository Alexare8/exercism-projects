from functools import cache


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target == 0:
        return []
    if target < 0:
        raise ValueError("target can't be negative")

    sorted_coins = sorted(coins, reverse=True)

    @cache
    def find_coins(target: int) -> list[int] | None:
        if all(target < coin for coin in sorted_coins):
            return None
        potential_change: list[int] = []
        for coin in sorted_coins:
            if target == coin:
                return [coin]
            if target > coin:
                result = find_coins(target - coin)
                if result != None and (
                    potential_change == [] or len(potential_change) > len(result) + 1
                ):
                    potential_change = result + [coin]

        if potential_change == []:
            return None
        return potential_change

    shortest_change = find_coins(target)

    if shortest_change == None:
        raise ValueError("can't make target with given coins")

    return sorted(shortest_change)
