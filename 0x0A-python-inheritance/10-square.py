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

    def area(self):
        """returns the area"""
        return self.__height * self.__width

    def __str__(self):
        """returns a string"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Square method"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2
