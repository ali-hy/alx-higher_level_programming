#!/bin/bash
# this is a script prints the http after making a response to the specified URL
curl -s -o /dev/null -w "%{http_code}" "$1"
