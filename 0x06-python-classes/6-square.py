#!/usr/bin/python3
"""Square module that defines a square by attributes and methods in (based on 5-square.py)"""


class Square:
    """A class square with size atrribute
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """initializes a Square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        """to ensure size is an integer"""
        self.__size = size

    def area(self):
        """calculates the area of the square which is size ** 2
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """a getter allows us to refers to the fields
        Returns: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """a setter allows to input correct values like needed"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0, position=(0, 0)):
        """determines the position of the square using coordinates
        Args:
            position (int)
        Returns: None
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ a getter of __position"""
    return self.__position

    @position.setter
    def position(self, value):
        """ a setter of __position"""
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the square with the # character on stdout."""
        if self.__size == 0:
            print("")
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
