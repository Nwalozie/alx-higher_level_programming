#!/bin/usr/python3
#2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Function that replaces an element of a list at a specific position."""
    if idx < 0 or idx > (len(my_list)-1):
        return my_list
    return  my_list[idx] = element