#!/bin/usr/python3
def text_indentation(text):
    if isinstance(text, str):
        lent = len(text)
        counter = 0
        while counter < lent:
            print(text[counter], end="")
            if text[counter] in ".:?":
                print("\n")
                counter += 1
            counter += 1
        print("\n")
    else:
        raise TypeError("text must be a string")
