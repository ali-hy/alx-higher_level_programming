#!/bin/bash
# This script sends a POST request to the URL passed as the first argument
response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1")
echo "Status code: $response"
