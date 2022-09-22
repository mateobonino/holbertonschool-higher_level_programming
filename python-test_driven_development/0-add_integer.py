#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """Adds two integers"""

    if b is None:
        errmsg = "add_integer() missing 1 required positional argument: 'b'"
        raise TypeError(errmsg)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
