#!/usr/bin/python3
"""Module for REctangle"""


class Rectangle:
    """
    Represents a rectangle.

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
        __str__(): Returns a string representation of the rectangle
        using print_symbol.
        __repr__(): Returns a string representation of the rectangle
        for object recreation.
        __del__(): Prints a farewell message when an instance is deleted.
        bigger_or_equal(rect_1, rect_2): Static method that returns the
        bigger rectangle based on area.
        square(cls, size=0): Class method that returns a new Rectangle instance
        with width == height == size.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

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
        """Returns a string representation of the rectangle
        using print_symbol.

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
        """Returns a string representation of the rectangle for
        object recreation.

        Returns:
            str: A string representation of the rectangle.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a farewell message when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return the bigger rectangle based on area.

        Args:
            rect_1 (Rectangle): An instance of Rectangle.
            rect_2 (Rectangle): Another instance of Rectangle.

        Returns:
            Rectangle: The bigger rectangle or rect_1 if both have the
            same area value.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to create a square instance.

        Args:
            size (int): The size of the square (default 0).

        Returns:
            Rectangle: A new Rectangle instance with width == height == size.

        """
        return cls(size, size)
