#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """Adds two integers"""
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    return (a + b)
