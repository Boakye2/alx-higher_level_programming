#!/usr/bin/python3
# 0-add_integer.py
""" File name : 0-add_integer.py
    Integers addition: function that adds two integers
    Prototype: def add_integer(a, b=98)
"""

def add_integer(a, b=98):
    """Return the integer addition of a and b.
    """
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
