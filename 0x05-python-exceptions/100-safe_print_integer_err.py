#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as en:
        print("Exception: {}".format(en), file=sys.stderr)
        return False
