#!/usr/bin/python3
for ascii_alp in range(ord("a"), ord("z") + 1):
  if chr(ascii_alp) not in ("q", "e"):
    print(chr(ascii_alp), end="")
