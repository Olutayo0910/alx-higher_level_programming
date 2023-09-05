#!/usr/bin/python3
"""Module for print square method"""


def print_square(size):
    """

    :param size: size of the square

    :raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    :return: prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
