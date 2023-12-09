#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers in reverse

    Args:
        my_list (list, optional): List item. Defaults to [].
    """
    new_list = []
    if len(my_list) < 1:
        return"None"
    for i in range(len(my_list)):
        popped = my_list.pop()
        new_list.append(popped)
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))
