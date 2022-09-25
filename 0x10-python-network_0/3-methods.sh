#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -i -L -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
