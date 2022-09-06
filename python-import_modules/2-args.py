#!/usr/bin/python3
import sys
argv_len = len(sys.argv) - 1
if argv_len == 1:
    print("1 argument:")
    print("1: {}".format(sys.argv[1:]))
elif argv_len == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(argv_len))
    for i in range(argv_len):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
