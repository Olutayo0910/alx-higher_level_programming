#!/usr/bin/python3
"""
Python script that takes in a URL and an email, post a request to the URL,
with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
import urllib.parse
from sys import argv


if len(argv) > 2:
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
