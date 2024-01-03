#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and
display the value of the X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
