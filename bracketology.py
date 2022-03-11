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

# Get the School name, conference, NET, record, and SoS
basicSchoolInfoList = websiteInfo.find_all("div", class_="ts-flex-size-1")

for basicSchoolInfo in basicSchoolInfoList:
    print(basicSchoolInfo.prettify())


