#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers in reverse

    Args:
        my_list (list, optional): List item. Defaults to [].
    """
    for i in range(len(my_list)):
        new_list = []
        popped = my_list.pop(my_list)
        new_list.append(popped)
        print(new_list)

print_reversed_list_integer([1, 2, 3, 4, 5])