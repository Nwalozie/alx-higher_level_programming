#!/bin/user/python3
#3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order."""
    count = 0
    for i in my_list:
        count-= 1
        print("{:d}".format(my_list[count]))
