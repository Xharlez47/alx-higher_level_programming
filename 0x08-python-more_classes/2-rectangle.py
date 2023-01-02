#!/usr/bin/python3
"""
    Defines a classs Rectangle
"""


class Rectangle:
    """A class Rectangle with width and height attributes
    Attributes:
        _width (int): width of Rectangle
        _height (int): height of Rectangle
    """
    def __init__(self, width=0, height=0):
        """initializes a Rectangle
        Args:
            _width (int): width of Rectangle
            _height (int): height of Rectangle
        Returns: None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter allows us to refers to the fields
        Returns: the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """a setter allows to input correct values like needed"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter allows us to refers to the fields
        Returns: the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """a setter allows to input correct values like needed"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the Rectangle which is width * height
        Returns:
            area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the Rectangle which is (width + height) * 2
        Returns:
            Perimeter of the Rectangle
        """
        if self.__width and self.__height == 0
            perimeter == 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter
