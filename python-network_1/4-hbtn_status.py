#!/usr/bin/python3
"""
    Fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import requests
    with requests.get("https://intranet.hbtn.io/status") as response:
        print("Body response:")
        print("\t- type: {}".format(type(response._content.decode())))
        print("\t- content: {}".format(response._content.decode()))
