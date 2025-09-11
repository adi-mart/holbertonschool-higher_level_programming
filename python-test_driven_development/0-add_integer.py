#!/usr/bin/python3
"""
Module that adds two integers.
Raises:
    TypeError: If either a or b is not an integer or float.
Returns:
    The sum of a and b as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
