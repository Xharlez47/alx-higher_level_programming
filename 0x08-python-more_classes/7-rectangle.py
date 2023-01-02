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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances += 1

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
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the square with # to stdout"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
