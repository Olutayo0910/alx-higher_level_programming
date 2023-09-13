#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """a function def pascal_triangle(n): that
    returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    triangle = []
    if n == 0:
        return triangle

    triangle.append([1])

    for i in range(1, n):
        before = triangle[-1]
        after = [1]
        for i in range(len(before) - 1):
            after.append(before[i] + before[i + 1])
        after += [1]
        triangle.append(after)

    return triangle
