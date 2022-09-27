#!/usr/bin/python3
"""Inherits from Function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    from the specified class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
