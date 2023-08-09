#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ''
    i = 0
    for c in str:
        if i != n:
            newStr += str[i]
        i += 1
    return newStr
