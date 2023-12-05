#!/usr/bin/python3
"""
Python script that fetches an URL
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    text = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(text), text))
