#!/bin/bash
# This script sends a POST request to the URL passed as the first argument
curl -s -o /dev/null -w "%{http_code}\n" "$1"
