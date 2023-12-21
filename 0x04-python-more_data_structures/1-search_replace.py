#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list

    Args:
        my_list : list
        search : occurence
        replace : replacemet value
    """
    new_list = my_list[:]
    new_list= list(map(lambda x: replace if x == search else x, new_list))
    print(new_list)
        
search_replace([1, 23, 4], 23, 3)