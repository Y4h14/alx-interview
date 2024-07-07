#!/usr/bin/python3
""" defines a solution for the Nqueen problem"""
import sys


def solve_nqueens(n):
    def backtrack(row):
        # check if we gone thro all rows
        if row == n:
            solutions.append([[c, r] for c, r in enumerate(board)])
        else:
            # add a possible solution then trackback if it's not valid
            for col in range(n):
                if is_vaild(row, col):
                    board[row] = col
                    backtrack(row + 1)

    def is_vaild(row, col):
        # check for in row, in col, or diagnal placement
        for r in range(row):
            if board[r] == col or \
               board[r] - r == col - row or \
               board[r] + r == col + row:
                return False
        return True

    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
