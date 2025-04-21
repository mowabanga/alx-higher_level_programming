#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        for i in range(len(my_list)):
            if idx < 0:
                return None
            elif idx > len(my_list):
                return None
            elif my_list[i] == idx:
                return("Element at index {:d} is {}".format(idx, my_list[idx]))
            
print(element_at([1, 2, 3, 4, 5], 2))