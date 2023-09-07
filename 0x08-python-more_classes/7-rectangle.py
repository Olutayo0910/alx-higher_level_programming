#!/usr/bin/python3
"""Module for rectangle"""


class Rectangle:
    """Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): The number of rectangle instances created.
        print_symbol: The symbol used to represent the rectangle
        when printing.

    Methods:
        area(): Calculates and returns the area of the rectangle.
        perimeter(): Calculates and returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the
        rectangle using print_symbol.
        __repr__(): Returns a string representation of the
        rectangle for object recreation.
        __del__(): Prints a farewell message when an instance is deleted.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        return 0 if self.__width == 0 or self.__height == 0 \
            else 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the
        rectangle using print_symbol.

        Returns:
            str: A string representation of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle
        for object recreation.

        Returns:
            str: A string representation of the rectangle.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a farewell message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
