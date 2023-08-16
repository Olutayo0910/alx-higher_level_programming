#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1_diff = set_1.difference(set_2)
    set2_diff = set_2.difference(set_1)

    result = set1_diff.union(set2_diff)

    return result
