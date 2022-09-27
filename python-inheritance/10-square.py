#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
