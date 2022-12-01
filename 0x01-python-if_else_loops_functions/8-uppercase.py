#!/usr/bin/python3

def uppercase(c):
    d = ""
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            d += i.upper() 
        else:
            d += i
    print(d)
