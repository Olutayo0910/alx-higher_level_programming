#!/usr/bin/python3
"""Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """

    :param my_obj: the object to be written
    :param filename: the file into which the obj is written
    :return: the new file
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(my_obj, fp)
