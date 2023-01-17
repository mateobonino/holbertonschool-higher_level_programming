#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in
the header of the response
"""
import urllib.request
import sys.argv

with urllib.request.urlopen(argv[1]) as response:
    body = response.info()
    print(body["X-Request-Id"])
