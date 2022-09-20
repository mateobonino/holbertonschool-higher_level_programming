#!/usr/bin/python3
"""Script that creates a Square named class"""


class Square():
    """"Defines a square"""
    __size = None

    def __init__(self, size=0):
        self.__size = size

    @propety
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines the value of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
