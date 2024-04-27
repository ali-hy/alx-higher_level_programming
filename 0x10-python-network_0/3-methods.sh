#!/bin/bash
# This script sends an OPTIONS request to the URL passed as the first argument and displays the allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
