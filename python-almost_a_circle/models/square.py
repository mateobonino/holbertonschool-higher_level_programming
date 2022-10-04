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
