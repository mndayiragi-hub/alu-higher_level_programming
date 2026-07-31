#!/usr/bin/python3
"""Module that displays X-Request-Id using requests"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
