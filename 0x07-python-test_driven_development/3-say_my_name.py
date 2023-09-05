#!/usr/bin/python3
"""Module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """

    :param first_name: first name to say
    :param last_name: second name to say

    :raises:
        TypeError first_name must be a string or
        last_name must be a string
    :return: prints My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
