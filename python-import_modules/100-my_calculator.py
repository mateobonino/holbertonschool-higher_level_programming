#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    argv_len = len(sys.argv) - 1
    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] == "+":
        result = sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' '
        print("{}=".format(result), end=" ")
        print("{}".format(add(int(sys.argv[1]), int(sys.argv[3]))))
    elif sys.argv[2] == "-":
        result = sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' '
        print("{}=".format(result), end=" ")
        print("{}".format(sub(int(sys.argv[1]), int(sys.argv[3]))))
    elif sys.argv[2] == "*":
        result = sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' '
        print("{}=".format(result), end=" ")
        print("{}".format(mul(int(sys.argv[1]), int(sys.argv[3]))))
    elif sys.argv[2] == "/":
        result = sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' '
        print("{}=".format(result), end=" ")
        print("{}".format(div(int(sys.argv[1]), int(sys.argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
