#!/bin/python3.9

import requests
from bs4 import BeautifulSoup

URL = "https://www.warrennolan.com/basketball/2022/team-net-sheet?team=Bellarmine"

page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
