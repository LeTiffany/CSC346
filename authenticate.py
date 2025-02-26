#! /usr/bin/python3

import requests
import passwords

username = passwords.username
password = passwords.password

requests.get("https://httpbin.org/basic-auth/tiffany/nugget", auth = (username, password))
