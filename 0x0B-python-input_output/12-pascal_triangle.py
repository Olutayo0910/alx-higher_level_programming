#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """a function def pascal_triangle(n): that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        previous = triangle[-1]
        new_row = triangle[1]

        for i in range(1, len(previous)):
            new_element = previous[i - 1] + previous[i]
