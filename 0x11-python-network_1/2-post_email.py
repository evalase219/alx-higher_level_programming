#!/usr/bin/python3
"""
Script that takes in a URL and sends a POST request
to the passed URL with email as a parameter
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    mail = sys.argv[2]
    # Perepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': mail}).encode('utf-8')
    # Send a POST request to the URL with the email as a parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the content of the response
        content = response.read().decode('utf-8')
    # Display the body of the response
    print(content)
