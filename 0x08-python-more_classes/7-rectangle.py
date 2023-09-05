#!/usr/bin/python3


class Rectangle:
    """
    This class defines a Rectangle object with width and height attributes.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): Keeps track of the
        number of instances of Rectangle.
        print_symbol (str): The symbol used for representing
        the rectangle when printed.

    Methods:
        area(): Calculate the area of the rectangle.
        perimeter(): Calculate the perimeter of the rectangle.
        __str__(): Return a string representation of the rectangle.
        __repr__(): Return a string representation of
        the rectangle for object recreation.
        __del__(): Destructor that gets called when an instance is deleted.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else 2 * (self.width + self.height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """
        Return a string representation of the rectangle for object recreation.

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor that gets called when an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
