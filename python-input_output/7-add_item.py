#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file == __import__('6-load_from_json_file').load_from_json_file

import sys
import json

try:
    items_list = load_from_json_file('add_item.json')
except:
    items_list = []
for i in range(1, len(sys.argv)):
    items_list.append(sys.argv[1])
save_to_json_file(items_list, 'add_item.json')

