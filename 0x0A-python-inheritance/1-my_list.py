#!/usr/bin/python3
"""
    the MyList class
"""


class MyList(list):
    """inherits a class list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
