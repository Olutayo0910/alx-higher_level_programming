#!/usr/bin/python3
"""creates an Object from a JSON file"""

import sys
import os.path

args = sys.argv[1:]

save_to_json_file = __import__(5-save_to_json_file).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file).load_from_json_file

item_list = []
if os.path.exists("./add_item.json"):
    item_list = load_from_json_file("add_item.json")
save_to_json_file(item_list + args, "add_item.json")
