#!/bin/usr/python3
#8-multiple_returns.py


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""
    if sentence != '':
        first_char = sentence[0]
    else:
        first_char = None
    tuple_ = (len(sentence), first_char)
    return(tuple_)
