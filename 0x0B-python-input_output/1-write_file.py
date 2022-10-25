#!/usr/bin/python3
"""Writing a string to an encoded file"""

def write_file(filename="", text=""):
    """write_file - function to write into a file
    @filename: name of file
    @text: string to be written into file"""
    
    with open(filename, encoded="UTF8") as ut:
        return ut.write(text)