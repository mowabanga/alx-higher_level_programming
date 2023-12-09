#!/usr/bin/python3
def element_at(my_list, idx):
    """ Retrieves an element from a list

    Args:
        my_list (_type_): list
        idx (_type_): index of element
    """
    length = len(my_list)
    if idx >= length or idx < 0:
        return "None"
    else:
        return my_list[idx]
