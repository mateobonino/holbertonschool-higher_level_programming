#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file == __import__('6-load_from_json_file').load_from_json_file

import sys
import json

items_list = []

try:
    with open('add_item.json', 'w') as f:
        items_list = load_from_json_file('add_item.json')
        for i in sys.argv[1:]:
            items_list.append(i)
        f.close()
except IOError:
    with open('add_item.json', 'w+') as f:
        items_list = load_from_json_file('add_item.json')
        for i in sys.argv[1:]:
            items_list.append(i)
        f.close()
