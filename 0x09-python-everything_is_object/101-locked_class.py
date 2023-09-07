#!/usr/bin/python3
"""LockedClass model"""


class LockedClass:
    """
    a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new
    instance attributes.
    """
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """
        :param first_name: the only slot
        """
        self.first_name = first_name
