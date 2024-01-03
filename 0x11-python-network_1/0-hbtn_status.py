#!/usr/bin/python3
"""
Fetch https://alx-intranet.hbtn.io/status using urllib package
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status")\
            as response:
        content = response.read()
        # Decode the byte content to a UTF-8 string
        content_str = content.decode('utf-8')
    # Display the content with tabulation before each line
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content_str))
