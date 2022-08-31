#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total = 0
    arguments = sys.argv

    for i in range(len(arguments) - 1):
        total += int(arguments[i + 1])
    print("{}".format(total))
