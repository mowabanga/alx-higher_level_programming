#!/bin/usr/python3
from sys import argv
arglen = len(argv) - 1
if arglen < 1 :
    print('0 arguments')
else:
    print('{} arguments:'.format(arglen))
    for i in range(len(argv[1:])):
        print('{}: {}'.format(i, argv[i]))