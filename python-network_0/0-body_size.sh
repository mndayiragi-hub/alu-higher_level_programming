#!/usr/bin/env bash
curl -s -o /dev/null -w "%{size_download}\n" "$1"
