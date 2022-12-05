#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix[0])
    col = len(matrix)
    i, j = 0, 0
    k = row - 1
    if (row > 0 and col > 0):
        while (i < col):
            while (j < row):
                print("{:d}".format(matrix[i][j]), end="")
                if (j < k):
                    print(" ", end="")
                j += 1
            i += 1
            j = 0
            print("\n", end="")
    else:
        return None
