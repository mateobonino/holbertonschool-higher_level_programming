#!/usr/bin/python3
"""
    Takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user
    with the letter as parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    if argv[1]:
        myData = {"q": argv[1]}
    else:
        myData = {"q": ""}
    url = "http://0.0.0.0:5000/search_user"
    with requests.post(url, data=myData) as response:
        try:
            myResponse = response.json()
        except Exception as invalid:
            print("Not a valid JSON")
        if len(list(myResponse.keys())) >= 2:
            print("[{}] {}".format(myResponse['id'], myResponse['name']))
        else:
            print("No result")
