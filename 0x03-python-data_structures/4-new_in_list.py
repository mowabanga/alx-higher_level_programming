#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx > len(my_list) or idx < 0:
        return my_list
    else:
        new_list[idx] = element
        return new_list
    
print(new_in_list([1, 2, 34, 4, 5], 10, 32))