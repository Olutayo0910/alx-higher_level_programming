#!/usr/bin/python3
"""module for append_write"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
    :param filename: the file to be appended to
    :return: the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as new_file:
        return new_file.write(text)
