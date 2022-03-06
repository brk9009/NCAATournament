import requests

# Making a GET request
r = requests.get('https://www.warrennolan.com/basketball/2022/team-net-sheet?team=Jacksonville-State')

# check status code for response received
# success code - 200
print(r.status_code)

# print content of request
print(r.content)
