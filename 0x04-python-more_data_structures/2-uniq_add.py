#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    adds = 0
    for num in unique:
        nums = int(num)
        adds += nums
    return adds
