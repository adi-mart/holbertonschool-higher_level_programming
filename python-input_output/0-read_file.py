#!/usr/bin/python3
"""
Module that contains a function to read a text file
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print it to stdout

    Args:
        filename (str): name of the file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
