
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        space = ""
        for j in l:
            print("{:s}{:d}".format(space, j), end="")
            space = " "
        print()
