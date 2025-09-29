#!/usr/bin/python3
"""
Module that contains a function to convert class to JSON
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: instance of a Class

    Returns:
        dict: dictionary representation of the object
    """
    return (obj.__dict__)
