#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a sepcific position

    Args:
        my_list (_list_): list
        idx (__int__): index
        element (_int_): element to replace
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
