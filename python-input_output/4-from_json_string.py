#!/usr/bin/python3
"""
Module that contains a function to convert JSON string to object
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): JSON string to convert to object

    Returns:
        object: Python data structure represented by JSON string
    """
    return (json.loads(my_str))
