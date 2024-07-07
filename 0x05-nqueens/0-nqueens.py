#!/usr/bin/python3
""" defines a solution for the Nqueen problem"""
import sys


def solve_nqueens(n, row, step, result):
    if row == n:
        result.append(step[:])
    else:
        for i in range(n):
            step.append(i)
            # print(step)
            if (isValid(step)):
                solve_nqueens(n, row+1, step, result)
            step.pop()


def isValid(step):
    """"""
    curr_row: int = len(step) - 1
    for i in range (curr_row):
        diff = abs(step[i] - step[curr_row])
        if diff == 0 or diff == curr_row - i:
            return False
    return True


if __name__ == "__main__":


    if len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])

    if not isinstance(N,int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    results = []
    solve_nqueens(N, 0, [], results)
    print(results)