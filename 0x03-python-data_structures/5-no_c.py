#1/usr/bin/python3
def no_c(my_string):
    """remove all 'c' and 'C'

    Args:
        my_string (_type_): string
    """
    updated_string = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            updated_string += i
    return updated_string
