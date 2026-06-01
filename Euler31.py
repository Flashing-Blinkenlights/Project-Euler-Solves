from functools import lru_cache


coins = [1, 2, 5, 10, 20, 50, 100, 200]

# observation: larger coins can be made up of smaller coins recursively

TARGET_VALUE = 200

possibilities = 0


@lru_cache
def coins_for_value(val, max_coin=coins[-1]):

    combinations = []
    if val in coins and val <= max_coin:  # a single coin can be used
        combinations.append([val])

    for coin in reversed(coins):
        if coin > val or coin > max_coin:
            continue
        combinations += [
            [coin] + combination for combination in coins_for_value(val - coin, coin)
        ]
    return combinations


for coin in coins:
    print(coin, len(coins_for_value(coin)))
