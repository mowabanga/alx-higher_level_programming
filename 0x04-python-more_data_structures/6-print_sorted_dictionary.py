#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionay by ordered keys

    Args:
        a_dictionary (_dict_): dictionary to be sported
    """
    sorted_dict = dict(sorted(a_dictionary.keys(), key=lambda x: x[0].upper()))
    return sorted_dict

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print(a_dictionary)