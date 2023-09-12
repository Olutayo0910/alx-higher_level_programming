#!/usr/bin/python3
"""module for add_attribute"""

def add_attribute(obj, attribute, value):
    """function that adds a new attribute to an object if it’s possible:"""
    if hasattr(obj, '__dict__') or \
            (hasattr(obj, '__slots__') and attribute in
             type(obj).__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
