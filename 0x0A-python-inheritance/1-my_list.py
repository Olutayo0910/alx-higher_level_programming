#!/usr/bin/python3
"""module for MyList"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class with additional methods.

    Public Methods:
    - print_sorted(): Prints the list in ascending sorted order.

    Attributes:
    - Inherits all attributes and methods from the list class.

    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
