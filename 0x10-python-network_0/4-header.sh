#!/bin/bash
# This script sends a GET request to the URL passed as the first argument, includes a header variable X-School-User-Id
curl -s -H "X-School-User-Id: 98" "$1"
