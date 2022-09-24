#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle():
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rarea = rect_1.area()
        r2area = rect_2.area()
        if rarea >= r2area:
            return rect_1
        if r2area >= rarea:
            return rect_2

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def area(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        string = ''
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for _ in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return string[:-1]
