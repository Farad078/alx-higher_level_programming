#!usr/bin/python3

def print_square(size):
    if isinstance(size, int):
        if size >= 0:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print("")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
