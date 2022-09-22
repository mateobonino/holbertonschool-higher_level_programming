#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    __size = 0
    __position = (0, 0)
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0"
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len position != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[0]):
            print(" ", end='')
        for j in range(self.__size):
            print("#", end="")
        print("")
