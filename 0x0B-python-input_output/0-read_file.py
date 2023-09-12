!/usr/bin/python3
"""module for read_file"""


def read_file(filename=""):
    """
    Args:
    :param filename: the file to be read
    :return: the content of the file
    """
    with open('filename', encoding='utf-8') as new_file:
        print(new_file.read())
