#!/usr/bin/python3
"""
Module that contains a function to save object to JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using a JSON representation

    Args:
        my_obj: object to save
        filename (str): name of the file to save to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
