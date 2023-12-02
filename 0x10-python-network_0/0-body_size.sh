#!/bin/bash
# script that takes in a URL, sends a request to that URL and display the size
curl -sI "$1" | grep -i "Content-length" | cut -d " " -f 2
