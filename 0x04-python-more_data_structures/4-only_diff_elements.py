#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """returns set of all elements present in only one set
    Args:
        set_1 (_type_): _description_
        set_2 (_type_): _description_
    """
    return set_1 ^ set_2
