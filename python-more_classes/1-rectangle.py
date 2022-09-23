#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle():
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
             ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self):
        return self.__width

    @height.setter
    def height(self):
        return self.__height



