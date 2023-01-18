#!/usr/bin/python3
"""
    Takes in a URL, sends a request to the URL
    and displays the body of the response
"""
if __name__ == "__main__":
    from urllib import error, request
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            myResponse = response.read().decode()
    except error.HTTPError as error:
        print("Error code: {}".format(error.__dict__['code']))
