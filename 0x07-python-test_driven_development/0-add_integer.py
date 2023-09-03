#!/usr/bin/python3
""" Function for adding integers """


def add_integer(a, b=98):
    """

    :param a: first integer
    :param b: second integer

    :raises:
        if a and/or b is not int or float

    :return: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b

    if __name__ == __main__:
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
