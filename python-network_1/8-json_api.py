#!/usr/bin/python3
"""Module that sends a search request to the API"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})

    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
