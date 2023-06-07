#!/usr/bin/python3
def uppercase(str):
    for j in range(len(str)):
        k = ord(str[j])
        if (k >= 97) and (k <= 122):
            k -= 32
        print("{}".format(chr(k)), end="")
    print()
