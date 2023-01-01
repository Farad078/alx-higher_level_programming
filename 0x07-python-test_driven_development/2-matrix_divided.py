#!/usr/bin/python3

def list_check(matrix):
    if isinstance(matrix, list):
        a = 1
        for i in matrix:
            if isinstance(i, list):
                a *= 1
            else:
                a *= 0
            for j in i:
                if isinstance(j, int) or isinstance(j, float):
                    a *= 1
                else:
                    a *= 0
    return a


def row_check(matrix):
    if isinstance(matrix, list):
        a, b = len(matrix[0]), 1
        for i in matrix:
            if len(i) == a:
                b *= 1
            else:
                b *= 0
        return b


def type_check(matrix):
    a = 1
    for i in matrix:
        for j in i:
            if isinstance(j, int) or isinstance(j, float):
                a *= 1
            else:
                a *= 0
    return a


def matrix_divided(matrix, div):
    b = []
    if (list_check(matrix) == 1) and (type_check(matrix) == 1):
        if row_check(matrix) == 1:
            if isinstance(div, int) or isinstance(div, float):
                if div != 0:
                    for i in matrix:
                        a = []
                        for j in i:
                            a.append(round(j / div, 2))
                        b.append(list(a))
                    return b
                else:
                    print(ZeroDivisionError("division by zero"))
            else:
                print(TypeError("div must be a number"))
        else:
            print(TypeError("Each row of the matrix must have the same size"))
    else:
        print(TypeError("matrix must be a matrix (list of lists) of integers"))
