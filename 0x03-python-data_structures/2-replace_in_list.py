#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a sepcific position

    Args:
        my_list (_list_): list
        idx (__int__): index
        element (_int_): element to replace
    """
    listlen = len(my_list)
    if idx > listlen or idx < 0:
        returns(my_list)
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
    print(my_list)
