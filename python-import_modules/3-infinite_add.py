#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1
    argv_sum = 0
    for i in range(argv_len):
        argv_sum += int(sys.argv[i + 1])
    print(argv_sum)
