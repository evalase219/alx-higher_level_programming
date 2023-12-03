#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the
URL and displays the body of the response.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":

    try:
        # Send a request to the URL and open a connection
        with urllib.request.urlopen(sys.argv[1]) as response:
            # Read and decode the content of the response
            content = response.read().decode('utf-8')
        # Display the body of the response
        print(content)
    except urllib.error.HTTPError as e:
        # Handle HTTPError exceptions
        print("Error code: {}".format(e.code))
