#!/usr/bin/python3
"""CSV to JSON conversion module."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format.

    Args:
        csv_filename (str): The CSV filename to read from

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, mode='r', newline='',
                  encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        csvfile.close()
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        jsonfile.close()
        return (True)
    except FileNotFoundError:
        return (False)
