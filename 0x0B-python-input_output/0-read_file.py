#!/usr/bin/python3

"""Python function to read contents of a text file and print them to standard output"""

def read_file(filename=""):
    """read_file - reads a text file and prints to standard output
    @filename: parameter"""
    
    with open(filename, encoding='UTF8') as ut:
        print(ut.read(), end='')