#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'r') as fp:
        return json.load(fp)
