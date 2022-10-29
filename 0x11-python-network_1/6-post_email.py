#!/usr/bin/python3
"""POST an email #1"""
import requests
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    req = requests.post(sys.argv[1], data={'Your email is': email})
    print(req.text)
