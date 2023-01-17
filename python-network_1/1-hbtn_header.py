#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    body = response.info()
print(body["X-Request-Id"])
