#!/usr/bin/python3
"""
    Python script that takes in a URL and email, sends a POST request to the URL
    with email as a parameter and displays the body of the response
    decoded in utf-8
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    reques = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(reques) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))
