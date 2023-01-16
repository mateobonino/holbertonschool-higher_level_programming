#!/bin/bash
# takes in a URL, sends a request to that URL
curl -si $1 | grep "length" | cut -d ' ' -f 2