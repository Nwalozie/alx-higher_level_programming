#!/bin/user/python3
#5-no_c.py


def no_c(my_string):
    """removes all characters c and C from a string."""
    lists = [x for x in my_string if x != 'c' and x != 'C']
    return("".join(lists))
