#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        for i in range(0, len(my_list)):
            print("{}".format(my_list[i]))
        
print_list_integer([1, 2, 3])