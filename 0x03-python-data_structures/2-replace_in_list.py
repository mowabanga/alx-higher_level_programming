#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        print(my_list)
        my_list[idx] = element
        return my_list
    
print(replace_in_list([1, 2, 3, 4], -1, 7))
        