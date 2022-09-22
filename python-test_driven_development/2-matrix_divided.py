#!/usr/bin/python3
"""Divides a matrix"""


def matrix_divided(matrix, div):
    """Divides a matrix"""
    if matrix is None:
        raise TypeError("matrix_divided() missing 1 required " +
                        "positional argument: 'matrix'")
    if div is None:
        raise TypeError("matrix_divided() missing 1 required " +
                        "positional argument: 'div'")
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    matrix_len = len(matrix[0])
    for i in matrix:
        if len(i) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
    for j in matrix:
        for k in j:
            if not isinstance(k, int) and not isinstance(k, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
    squared_matrix = []
    for i in matrix:
        squared_matrix.append([round(j / div, 2) for j in i])
    return squared_matrix
