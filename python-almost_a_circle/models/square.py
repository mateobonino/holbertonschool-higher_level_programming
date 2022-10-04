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
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size

    @height.setter
    def height(self, size):
        if not isinstance(size, int):
            raise TypeError("height must be an integer")
        if size <= 0:
            raise ValueError("height must be > 0")
        self.__height = size
