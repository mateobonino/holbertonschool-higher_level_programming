#!/usr/bin/python3
"""Is same class function"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of the class"""

    if isinstance(type(obj), a_class):
        return True
    else:
        return False
