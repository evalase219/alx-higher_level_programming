#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # Prepare the data to be sent in the POST request
    data = {'email': email}
    # Send a POST request to the url with the email as a parameter
    response = requests.post(url, data=data)
    # Display the body of the response
    print(response.text)
