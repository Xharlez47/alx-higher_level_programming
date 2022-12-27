#!/usr/bin/python3
"""defines a class a Square and has a private instance attribute called size"""


class Square:
    """A class square with size atrribute
       Attributes:
         __size (int): size of the square 
    """
    def __init__(self, size):
        """initializes a Square
        Args: size

        Returns: None
        """
        self.__size = size
