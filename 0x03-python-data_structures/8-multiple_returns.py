#!/bin/usr/python3
#8-multiple_returns.py


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""
    length = len(sentence)
    tuple_ = (length, sentence[0])
    
    return(tuple_)
