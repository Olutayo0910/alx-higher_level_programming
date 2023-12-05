#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub
API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        print(req.json().get('id'))
    except ValueError:
        print('Not a valid JSON')
