#!/usr/bin/pyhton3
def print_reversed_list_integer(my_list=[]):
    for nums in my_list[::-1]:
        print("{:d}".format(nums))
