#!/usr/bin/python3
"""module for MyList"""


def inherits_from(obj, a_class):
    """
    Checks  if the object is an instance of a class 
    that inherited (directly or indirectly) from the specified class
    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
