#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle:
    # Class attribute to keep track of the number of instances
    number_of_instances = 0
    # Class attribute to store the print symbol
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        # Initialize width and height with provided values
        self.width = width
        self.height = height
        # Increment the number of instances
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 0 if self.width == 0 or self.height == 0 else 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        # Decrement the number of instances when an instance is deleted
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
