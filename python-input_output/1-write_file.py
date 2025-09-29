#!/usr/bin/python3
"""
Module that contains a function to write to a text file
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number
    of characters written

    Args:
        filename (str): name of the file to write to
        text (str): text to write to the file

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
