#!/usr/bin/python3
"""
    a class MyList
"""


class MyList(list):
    """inherits the class list"""
    def __init__(self):
        """initializes the object"""
       super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
