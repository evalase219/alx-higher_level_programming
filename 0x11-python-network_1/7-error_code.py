#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    # Get the url from the command_line arguments
    url = sys.argv[1]
    # Send a request to the url
    response = requests.get(url)
    # Check if HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
