#!/usr/bin/python3
# Takes the response header from the URL
import urllib.request
import sys.argv

with urllib.request.urlopen(argv[1]) as response:
    body = response.info()
    print(body["X-Request-Id"])
