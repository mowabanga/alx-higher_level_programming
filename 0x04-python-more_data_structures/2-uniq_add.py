#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list

    Args:
        my_list (list, optional): _description_. Defaults to [].
    """
    unique_list = []
    sum = 0
    [unique_list.append(x) for x in my_list if x not in unique_list]
    for i in range(len(unique_list)):
        sum += unique_list[i]
        return sum
