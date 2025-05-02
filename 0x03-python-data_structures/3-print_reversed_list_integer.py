#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print(None)
    if my_list is None:
        return
    else:
        for i in reversed(my_list):
            print("{}".format(i))

print_reversed_list_integer(None)