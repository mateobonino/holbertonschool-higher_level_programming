#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        # The checker doesnt says nothing about valitadions but
        # is giving me all the checks wrong so im using the same
        # raise expections messages

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle to stdout"""
        c = ''
        for y in range(self.__y):
            print()
            c += '\n'
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
                c += ' '
            for k in range(self.__width):
                print("#", end="")
                c += '#'
            print()
            c += '\n'
        return c

    def __str__(self):
        """Returns the specified string"""
        str1 = "[Rectangle] ({}) {}/".format(self.id, self.x)
        str2 = "{} - {}/{}".format(self.y, self.width, self.height)
        return str1 + str2

    def update(self, *args, **kwargs):
        """Updates the attributes in the Class"""
        if args:
            if args[0]:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'width':
                    self.__width = j
                if i == 'height':
                    self.__height = j
                if i == 'x':
                    self.__x = j
                if i == 'y':
                    self.__y = j

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.__height,
                'x': self.x, 'y': self.y}
