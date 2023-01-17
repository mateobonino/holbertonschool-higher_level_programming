#!/bin/bash
# Displays all HTTP methods the server accepts
curl -vX OPTIONS $1 | grep -E "Allow" | cut -d ':' -f 2
