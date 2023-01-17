#!/usr/bin/python3
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    body = response.info()
print(body["X-Request-Id"])
