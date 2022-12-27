#!/usr/bin/python3
"""defines a class a Square and has a private instance attribute called size"""


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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
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
        self.__value = value
