#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square class attributes"""
        if args:
            if args[0]:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.__x = args[2]
            if len(args) > 3:
                self.__y = args[3]
        else:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'size':
                    self.__size = j
                if i == 'x':
                    self.__x = j
                if i == 'y':
                    self.__y = j

    def __str__(self):
        str1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        str2 = " - {}".format(self.height)
        return str1 + str2
