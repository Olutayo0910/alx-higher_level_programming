#!/usr/bin/python3
"""function json to object"""
import json


def from_json_string(my_str):
    """
    Convert JSON representation to a Python object.

    Args:
        my_str: a JSON string.
    Returns:
         returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
