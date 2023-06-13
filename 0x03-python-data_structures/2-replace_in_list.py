#!/usr/bin/python3
def replace_in_list(my_list, kdx, element):
    if kdx < 0 or kdx > (len(my_list) - 1):
        return (my_list)
    my_list[kdx] = element
    return (my_list)
