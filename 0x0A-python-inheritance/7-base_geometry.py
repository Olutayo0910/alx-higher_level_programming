#!/usr/bin/python3
"""module for empty class"""


class BaseGeometry:
    """a class with public instance"""
    def area(self):
        """

        :return: exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
