#!/usr/bin/python3
"""defines the makeChange function"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to
       meet a given total.

    Args:
        coins (List): a list of the values of the coins
        total (integer): total to be met

    Returns:
        integer: number of coins used
    """

    if total == 0:
        return 0

    coins.sort()
    reversed_coins = list(reversed(coins))
    count = 0

    if coins[0] > total:
        return -1

    while total > 0 and coins[0] <= total:
        # print(f"outer total {total}")
        for coin in reversed_coins:
            if coin <= total:
                total = total - coin
                # print(f"inner total {total}")
                count += 1
                break
    if total == 0:
        return count
    else:
        return -1
