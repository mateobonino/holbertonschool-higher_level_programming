#!/usr/bin/python3
"""Adds all arguments to a Python list"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file == __import__('6-load_from_json_file').load_from_json_file

import sys
import json

items_list = []

with open('add_item.json', 'w+') as f:
    items_list = load_from_json_file(f)

for i in sys.argv[1]:
    items_list.append(i)
save_to_json_file(items_list, 'add_item.json')
