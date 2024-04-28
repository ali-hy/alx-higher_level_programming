#!/usr/bin/python3
'''This script takes your GitHub credentials (username and password) and uses the GitHub API to display your id'''
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    password = sys.argv[2]
    response = requests.get(url, headers={'Authorization': 'Bearer {}'.format(password)})
    print(response.json().get('id'))
