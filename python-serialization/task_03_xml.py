#!/usr/bin/python3
"""XML serialization and deserialization module."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML format.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data to
    """
    root = ET.Element("root")
    for key, value in dictionary.items():
        new_element = ET.SubElement(root, key)
        new_value = str(new_element)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML data back to a Python dictionary.

    Args:
        filename (str): The filename to read XML data from

    Returns:
        dict: The deserialized Python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dict = {}
    for element in root:
        dict[element.tag] = element.text
    return (dict)
