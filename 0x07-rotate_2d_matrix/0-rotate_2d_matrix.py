#!/usr/bin/python3
"""defines a python function to reverse a 3D array"""


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix"""

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(len(matrix)):
        matrix[i].reverse()
