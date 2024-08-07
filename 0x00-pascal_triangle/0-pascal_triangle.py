#!/usr/bin/python3
"""defines a pascal triangle function"""


def pascal_triangle(n):
    """
    returns the nth row in the pascal triagle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    else:
        result = pascal_triangle(n - 1)
    row = [1]
    prev = result[-1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i+1])
    row += [1]
    result.append(row)
    return result
