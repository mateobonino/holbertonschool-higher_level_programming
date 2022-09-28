#!/usr/bin/python3
"""Returns a list with Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list with Pascal's triangle"""
    triangle = []
    if n <= 0:
        return triangle

    for i in range(0, n):
        fact = []
        for j in range(i + 1):
            fact.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(fact)
    return triangle


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
