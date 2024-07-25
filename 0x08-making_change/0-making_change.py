#!/usr/bin/python3


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total"""

    if total == 0:
        return 0

    coins.sort()
    reversed_coins = list(reversed(coins))
    count = 0

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
