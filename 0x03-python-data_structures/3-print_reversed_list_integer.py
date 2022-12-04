#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    j = -1 * i
    new_list = my_list.copy()
    k = 1
    while (j <= -1):
        my_list[-k] = new_list[j]
        j += 1
        k += 1
    for item in my_list:
        print("{:d}".format(item))
