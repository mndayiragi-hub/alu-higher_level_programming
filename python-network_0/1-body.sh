#!/bin/bash
# Display the body of a 200 status code GET response
curl -s -L -o /tmp/body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body
