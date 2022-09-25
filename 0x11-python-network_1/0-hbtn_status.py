#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib import request

    thehtml = ""
    theurl = "https://alx-intranet.hbtn.io/status"
    req = request.Request(theurl)
    with request.urlopen(req) as response:
        thehtml = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(thehtml)))
        print("\t- content: {}".format(thehtml))
        print("\t- utf8 content: {}".format(thehtml.decode('utf-8')))
