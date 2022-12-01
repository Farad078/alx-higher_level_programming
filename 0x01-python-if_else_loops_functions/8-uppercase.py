#!/usr/bin/python3

def uppercase(c):
    d = ''
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            d += chr(ord(i) - 32) 
        else:
            d += i
    print(d)
