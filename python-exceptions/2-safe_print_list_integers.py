#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for X in range(x):
        try:
            print("{:d}".format(my_list[X]), end="")
            count += 1
        except (IndexError, ValueError):
            pass
    print()
    return (count)
