#!/usr/bin/python3
"""
    Takes your Github credentials and uses the
    GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    myCreds = (argv[1], argv[2])
    url = "https://api.github.com/user"
    with requests.get(url, auth=myCreds) as response:
        try:
            toJson = response.json()
            print("{}".format(toJson['id']))
        except Exception as exc:
            print("None")
