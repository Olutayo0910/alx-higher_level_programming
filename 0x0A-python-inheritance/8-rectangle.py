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
        """integer validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialise width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
