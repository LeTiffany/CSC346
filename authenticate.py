#! /usr/bin/python3

import requests
import passwords

username = passwords.username
token = passwords.token

url = f"https://api.github.com/users/{username}"

response = requests.get(url, auth = (username, token))

print("Status: " + str(response.status_code))
print(response.text)
