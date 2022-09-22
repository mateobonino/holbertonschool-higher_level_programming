#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """Prints a square"""
    if type(size) is not int or size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for k in range(size):
            print("#", end='')
        print("")
