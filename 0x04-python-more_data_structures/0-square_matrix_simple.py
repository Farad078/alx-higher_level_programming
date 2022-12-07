#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    row = len(matrix)
    col = len(matrix[0])
    a = []
    i = 0

    while (i < row):
        j = 0
        b = []
        while (j < col):
            b.append(matrix[i][j] * matrix[i][j])
            j += 1
        a.append(b)
        i += 1
    return a
