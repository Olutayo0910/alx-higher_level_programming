#!/usr/bin/python3
"""
10-class_to_json.py
functions: class_to_json
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure """

    data = {}
    if hasattr(obj, "__dict__"):
        data = obj.__dict__.copy()
    return data
