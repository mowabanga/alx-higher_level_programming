#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    args = sys.argv
    if count == 0:
         print("0 arguments.")
    elif count  == 1:
        print("1 argument:")
        print("{:d}: {}".format(count, args[count]))
    else:
        print("{} arguments:".format(count))
        for i in range(len(args)):
            i = i + 1
            print("{}: {}".format(i, args[i]))
