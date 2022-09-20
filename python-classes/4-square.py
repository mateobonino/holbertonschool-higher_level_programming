#!/usr/bin/python3
"""Define a class Square."""


class Square():
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        size (int): The size of the new square"""
        self.__size = size

    @propety
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value.""""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
