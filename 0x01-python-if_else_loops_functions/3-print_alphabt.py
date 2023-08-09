#!/usr/bin/python3
for ascii_alp in range(ord("a"), ord("z") + 1):
    if ascii_alp != ord('e') and ascii_alp != ord('q'):
        print("{:c}".format(ascii_alp), end="")
