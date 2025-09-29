#!/usr/bin/python3
"""
Module that contains a function to load object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    Create an Object from a "JSON file"

    Args:
        filename (str): name of the JSON file to load from

    Returns:
        object: Object created from JSON file
    """
    with open(filename, 'r') as f:
        return (json.load(f))
