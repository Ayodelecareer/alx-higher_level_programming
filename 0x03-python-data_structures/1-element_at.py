#!/usr/bin/python3
def element_at(my_list, kdx):
    if kdx < 0 or kdx > (len(my_list) - 1):
        return None
    return (my_list[kdx])
