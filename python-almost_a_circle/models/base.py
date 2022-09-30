#!/usr/bin/python3
"""Base class"""


class Base():
    """Base clase"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            __nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
