#!/usr/bin/python3


def add_integer(a, b=98):
    if (isinstance(a, str) and isinstance(b, str)):
        return a + b
    elif not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    elif (isinstance(a, float) and isinstance(b, float)):
        c = int(a) + int(b)
        return float(c)
    else:
        return (int(a) + int(b))
