#!/usr/bin/python3
"""
    Takes in a URL, sends a request
    to the URL and displays the body
    of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    with requests.get(argv[1]) as response:
        if response.status_code < 400:
            print(response._content.decode())
        else:
            print("Error code: {}".format(response.status_code))
