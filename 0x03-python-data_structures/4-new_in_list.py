#!/usr/bin/python3
def new_in_list(my_list, jdx, element):
    if jdx < 0 or jdx > (len(my_list) - 1):
        return (my_list[:])
    new_list = my_list[:]
    new_list[jdx] = element
    return (new_list)
