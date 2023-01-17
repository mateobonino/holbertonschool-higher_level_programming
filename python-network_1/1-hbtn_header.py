#!/usr/bin/python3
"""
    Get the value of the X-Request-Id
    variable in the response headers
    of the passed URL
"""
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    body = response.info()["X-Request-Id"]
print(body)
