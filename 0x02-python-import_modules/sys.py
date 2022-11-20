#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, str(sys.argv[0])))