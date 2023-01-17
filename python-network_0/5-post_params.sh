#!/bin/bash
# Send various headers to an URL
curl -sX GET $1 -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
