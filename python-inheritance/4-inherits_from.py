#!/usr/bin/python3
"""Inherits from Function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
    from the specified class
    """
    if not isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
