#!/usr/bin/python3
"""module for MyList"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
