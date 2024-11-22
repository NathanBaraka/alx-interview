#!/usr/bin/python3
"""2D matrix rotation module.

This module contains a function to rotate an n x n matrix 90 degrees clockwise in place.
"""

def rotate_2d_matrix(matrix):
    """Rotates an n x n matrix 90 degrees clockwise in place.

    Args:
        matrix (list of lists): The n x n 2D matrix to rotate.
    """
    if not matrix or type(matrix) != list or not all(isinstance(row, list) for row in matrix):
        return

    n = len(matrix)
    
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()


