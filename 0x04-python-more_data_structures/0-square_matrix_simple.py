#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = []
    for x in matrix:
        matrix.append(list(map(square, matrix, x)))
    return (matrix)
