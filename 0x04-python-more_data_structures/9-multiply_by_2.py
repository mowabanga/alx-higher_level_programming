#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copied_dict = a_dictionary.copy()
    for key, value in copied_dict.items():
        value *= 2
    return (f"{key}: {value}")
