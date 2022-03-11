#!/bin/python3.9

import requests
from bs4 import BeautifulSoup

URL = "https://www.warrennolan.com/basketball/2022/team-net-sheet?team=Bellarmine"

# Get the HTML data
page = requests.get(URL)

# print(page.text)
# Create a BeautifulSoup object that uses the html parser to parse the page.
soup = BeautifulSoup(page.content, "html.parser")

# Find the team's information from the "container-x" id
websiteInfo = soup.find(id="container-x")
#print(websiteInfo.prettify())

# Find the net sheet from the "ts-container" class in "container-x"
netSheet = websiteInfo.select_one(".ts-container")
print(netSheet.prettify())


