#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    Args:
        my_list : list
        idx : index
        element : element
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
