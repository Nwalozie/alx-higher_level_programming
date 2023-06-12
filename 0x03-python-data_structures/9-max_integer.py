#!/bin/usr/python3
#9-max_integer.py


def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    a = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if a <= i:
                a = i

    return(a)

