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

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    remaining_total = total

    for coin in coins:
        if coin <= remaining_total:
            num_coins = remaining_total // coin
            remaining_total -= num_coins * coin
            count += num_coins

    return count if remaining_total == 0 else -1
