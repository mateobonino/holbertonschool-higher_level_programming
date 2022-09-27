#!/usr/bin/python3
"""
SAMPLE TEXT
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """SAMPLE TEXT
    a
    b
    c
    d
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
