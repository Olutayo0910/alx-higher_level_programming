#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides elements of matrix by div

    :param matrix: The matrix to be divided
    :param div: The number used to divide

    :raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero

    :return: another matrix
    """
    if not isinstance(matrix, list) and len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    row_length = []
    for row in matrix:
        x = len(row)
        row_length.append(x)
        if not all(size == row_length[0] for size in row_length):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
