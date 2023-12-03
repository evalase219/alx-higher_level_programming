#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header using request
package
"""
import requests
import sys

if __name__ == "__main__":
    # Send a request to the URL
    response = requests.get(sys.argv[1])
    # Check if the request was successful (status code 200)
    response.raise_for_status()
    # Get the value of the X-Request-Id variable from the response
    x_request_id = response.headers.get("X-Request-Id")
    # Display the value of X-Request-Id
    print(x_request_id)
