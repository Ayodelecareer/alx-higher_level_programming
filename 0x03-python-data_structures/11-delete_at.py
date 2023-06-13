#!/usr/bin/python3
def delete_at(my_list=[], kdx=0):
    if kdx < 0 or kdx > (len(my_list) - 1):
        return (my_list)
    del my_list[kdx]
    return (my_list)
