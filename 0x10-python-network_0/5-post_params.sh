#!/bin/bash
# This script sends a POST request to the URL passed as the first argument, includes variables email and subject in the request body, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
