#!/usr/bin/python3
""" add_attribute module """


def add_attribute(1object,1name, 1value):
    """ add_attribute function """
    if not hasattr(1object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(1object, 1name, 1value)
