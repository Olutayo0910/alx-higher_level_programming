#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = sum(score * weight for score, weight in my_list)
    denumerator = sum(weight for _, weight in my_list)
    result = numerator / denumerator
    return result
