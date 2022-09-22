#!/usr/bin/python3
"""Divides a matrix"""


def matrix_divided(matrix, div):
    """Divides a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    matrix_len = len(matrix[0])
    for i in matrix:
        if len(i) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
    for j in matrix:
        if not isinstance(j, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        for k in j:
            if type(k) is not int and type(k) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
    squared_matrix = []
    for i in matrix:
        squared_matrix.append([round(j / div, 2) for j in i])
    return squared_matrix
