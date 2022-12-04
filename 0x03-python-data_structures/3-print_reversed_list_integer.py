#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    j = -1 * i
    new_list = my_list.copy()
    k, l = 0, -1

    while (l >= j):
        my_list[k] = new_list[l]
        l -= 1
        k += 1
    for item in my_list:
        print("{:d}".format(item))


