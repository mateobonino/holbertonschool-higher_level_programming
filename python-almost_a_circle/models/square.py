#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(self, width, height, x, y, id)

    def __str__(self):
        str1 = "[Square] ({}) {}/{}".format(self.id, self.__x, self.__y)
        str2 = " - {}".format(self.__height)
        return str1 + str2
