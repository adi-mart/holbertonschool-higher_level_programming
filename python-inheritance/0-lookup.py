#!/usr/bin/python3
"""Module that defines a function to lookup attributes and
methods of an object."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return (dir(obj))
