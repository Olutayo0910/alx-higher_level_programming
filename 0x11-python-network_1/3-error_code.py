#!/usr/bin/python3
"""takes url & email, sends a request, displays the response"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            reed = response.read()
            print(reed.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
