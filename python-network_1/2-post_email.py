#!/usr/bin/python3
"""
    Takes in a URL and an email
    sends a POST request to the passed
    URL with the email as a parameter,
    and displays the body of the response
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    myData = {"email": argv[2]}
    parseData = parse.urlencode(myData).encode(())
    myRequest = request.Request(argv[1], data=parseData)
    with request.urlopen(myRequest) as response:
        decodeData = response.read().decode('UTF-8')
        print(decodeData)
