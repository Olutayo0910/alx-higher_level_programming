#!/usr/bin/python3
"""function for converting to json"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation as a string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON representation of the input object as a string.
    """
    json_string = json.dumps(my_obj)
    return json_string
