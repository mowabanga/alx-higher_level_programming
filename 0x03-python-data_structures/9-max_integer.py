#!/usr/bin/python3
def max_integer(my_list=[]):
    control = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if my_list[i] > control:
                control = my_list[i]
    return control
