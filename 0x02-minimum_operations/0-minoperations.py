#!/usr/bin/python3
"""defines a function for minimum oeprations"""


def minOperations(n: int) -> int:
    """reutns the fewest number of operations needed"""
    operations: int = 0
    curr: int = n

    while curr > 1:
        for i in range(2, curr + 1):
            if curr % i == 0:
                operations += i
                curr //= i
                break

    return operations
