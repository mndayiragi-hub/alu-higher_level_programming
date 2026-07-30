#!/usr/bin/env bash
response=$(curl -s -w "\n%{http_code}" "$1")
body=$(echo "$response" | head -n -1)
status=$(echo "$response" | tail -n 1)
if [ "$status" -eq 200 ]; then
    echo -n "$body"
fi
