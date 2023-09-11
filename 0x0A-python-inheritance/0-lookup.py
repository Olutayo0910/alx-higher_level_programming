#!/usr/bin/python3
"""module for lookup(obj)"""


def lookup(obj):
    """
    Args
    :param obj: Objects to look up
    :return: return the list of available attributes and methods of an object
    """
    return dir(obj)
