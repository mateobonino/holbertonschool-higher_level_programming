#!/usr/bin/python3
"""Base Geometry Class"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Defines a square that inherits from Rectangle class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
