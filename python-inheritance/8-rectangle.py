#!/usr/bin/python3
"""Base Geometry Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        self.integer_validator(height)
        self.integer_validator(width)
        self.__height = height
        self.__width = width
