#!/usr/bin/python3
"""
    a class Mylist
"""


class Mylist(list):
    """inherits the class list"""
    def __init__(self):
        """initializes the object"""
       super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
