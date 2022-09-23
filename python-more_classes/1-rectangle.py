#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle():
    """Defines a rectangle"""
    def __init__(self, width, height):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
                raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

