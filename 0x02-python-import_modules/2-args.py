#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    arglen = len(argv) - 1
    if arglen < 1 :
        print('0 arguments')
    else:
        print('{} arguments:'.format(arglen))
        for i in range(arglen):
            print('{}: {}'.format(i + 1, argv[i + 1]))