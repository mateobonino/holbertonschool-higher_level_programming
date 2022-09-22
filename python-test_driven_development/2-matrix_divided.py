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
    squared_matrix = []
    for i in matrix:
        squared_matrix.append([j / div for j in i])
    return squared_matrix