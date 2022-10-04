#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        str1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        str2 = " - {}".format(self.height)
        return str1 + str2

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        @width.setter
    def width(self, width):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value