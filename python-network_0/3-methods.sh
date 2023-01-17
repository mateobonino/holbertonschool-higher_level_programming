#!/bin/bash
# Displays all HTTP methods the server accepts
curl -siX OPTIONS $1 | grep "Allow" | cut -d ' ' -f 2-
