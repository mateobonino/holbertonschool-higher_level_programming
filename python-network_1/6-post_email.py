#!/usr/bin/python3
"""
    Takes in a URL and an email address,
    sends a POST request to the passed URL
    with the email as a parameter, and finally
    displays the body of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    params = {'email': argv[2]}
    forJson = {'email': argv[2]}
    with requests.post(url=argv[1], params=params, json=forJson) as req:
        print("Email: {}".format(argv[2]))
