#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    arglen = len(argv) - 1
    sum = 0
    if arglen < 1:
        print('0')
    elif arglen == 1:
        print("{}".format(argv[1]))
    else:
        for i in range(arglen):
            sum += int(argv[i + 1])
        print(sum)
