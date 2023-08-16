#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []

    for row in matrix:
        squared_row = []

        for element in row:
            squared_value = element ** 2
            squared_row.append(squared_value)

        square_matrix.append(squared_row)
    return square_matrix
