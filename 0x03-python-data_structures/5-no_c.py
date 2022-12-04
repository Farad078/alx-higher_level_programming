def no_c(my_string):
    a = ""
    for i in my_string:
        if ((i == 'c') or (i == 'C')):
            a += ''
        else:
            a += i
    return a
