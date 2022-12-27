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
        self.__size = size
        """to ensure size is an integer"""
        assert type(size) == int
        if size is not int
            except TypeError:
                print("size must be an integer")
        if size < 0
            except ValueError:
                print("size must be >= 0")
