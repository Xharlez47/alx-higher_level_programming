#!/usr/bin/python3
"""Square module that defines a square by attributes and methods in (based on 5-square.py)"""


class Square:
    """A class square with size atrribute
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """determines the position of the square using coordinates
        Args:
            position (tuple)
            size (int)
        Returns: None
        """
        self.size = size
        self.position = position

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

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character on stdout"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
