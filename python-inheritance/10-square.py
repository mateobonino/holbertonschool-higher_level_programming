#!/usr/bin/python3
"""Square class that inherits from Rectangle and Base Geomatry Class"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Defines a square that inherits from 'integer_validator' function
    from Rectangle and Base Geometry Class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
