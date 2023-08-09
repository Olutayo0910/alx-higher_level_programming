#!/usr/bin/python3
for ascii_value in range(ord('z'), ord('a') - 1, -1):
    print(chr(ascii_value).lower() if (ord('z') - \
    ascii_value) % 2 == 0 else chr(ascii_value).upper(), end='')
