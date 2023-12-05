#!/usr/bin/python3
"""Takes URL, sends a request, displays the value of X-Request-Id"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get(argv[1])
    print(req.headers.get('x-Request-Id'))
