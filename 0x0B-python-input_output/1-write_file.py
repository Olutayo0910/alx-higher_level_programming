#!/usr/bin/python3
"""module for write_file"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    and returns the number of characters

    Args:
    :param filename: the file to be read
    :return: the content of the file
    """
    with open(filename, mode='w', encoding='utf-8') as new_file:
        return new_file.write(text)
