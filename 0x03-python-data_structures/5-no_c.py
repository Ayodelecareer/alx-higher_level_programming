
#!/usr/bin/python3
def no_c(my_string):
    slist = list(my_string)
    [slist.remove(k) for k in slist if k == 'c' or k == 'C']
    return("".join(slist))
