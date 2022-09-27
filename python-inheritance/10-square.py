#!/usr/bin/python3
"""Defines a class named Square"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initializes the square
        
        size: the square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
