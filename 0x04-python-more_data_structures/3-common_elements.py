#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns common elements in the two sets

    Args:
        set_1 (list): set 1
        set_2 (list): set 2
    """
    c_elemen = set_1 & set_2
    return list(c_elemen)
