#!/usr/bin/python3
""" a Python script that fetches"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    req = "Body response:\n\t- type: {}\n\t- content: {}"
    print(req.format(type(response.text), response.text))
