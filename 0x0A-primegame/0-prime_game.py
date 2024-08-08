#!/usr/bin/python3
"""defines a function that determines the winner"""


def isWinner(x, num):
    """determine the winner based on the number of rounds"""

    if not num or x <= 0:
        return None
    max_n = max(num)

    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for start in range(2, int(max_n ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False

    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in num:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
