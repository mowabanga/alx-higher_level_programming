#!/usr/bin/python3
def number_keys(a_dictionary):
    """returns number of keys in a dictionary

    Args:
        a_dictionary (dictionary): dictionary
    """
    keys = []
    for key, value in a_dictionary.items():
        keys.append(key)
    return keys
