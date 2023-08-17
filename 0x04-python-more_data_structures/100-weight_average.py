#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    else:
        numerator = sum(score * weight for score, weight in my_list)
        denominator = sum(weight for _, weight in my_list)
        result = numerator / denominator
    return result
