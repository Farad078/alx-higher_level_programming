#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)

    if (i < 2 and i > 0):
        x = list(tuple_a)
        x.append(0)
        tupel_a = tuple(x)
    elif (i == 0):
        x = list(tuple_a)
        x.append(0)
        x.append(0)
        tuple_a = tuple(x)
    if (j < 2 and j > 0):
        x = list(tuple_b)
        x.append(0)
        tuple_b = tuple(x)
    elif (j == 0):
        x = list(tuple_b)
        x.append(0)
        x.append(0)
        tuple_b = tuple(x)

    a = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return a
