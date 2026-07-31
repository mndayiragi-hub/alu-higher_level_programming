#!/bin/bash
# Display all HTTP methods the server accepts
curl -s -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d " " -f2-
