import requests
from bs4 import BeautifulSoup

from teams import team_urls

#urls = ["https://www.warrennolan.com/basketball/2022/team-net-sheet?team=Bellarmine"]

#class NetSheetParser():
def scrape_net(url):

    # Get the HTML data
    page = requests.get(url)

    # print(page.text)
    # Create a BeautifulSoup object that uses the html parser to parse the page.
    soup = BeautifulSoup(page.content, "html.parser")

    # Find the team's information from the "container-x" id
    websiteInfo = soup.find(id="container-x")
    #print(websiteInfo.prettify())

    # Get the School name, conference, NET, record, and SoS
    #basicSchoolInfoList = websiteInfo.find_all("div", class_="ts-flex-size-1")

    #for basicSchoolInfo in basicSchoolInfoList:
    #    print(basicSchoolInfo.prettify())
    
    # Parse the team name, conference, and record
    teamBasics = websiteInfo.find("div", class_="ts-teamname")
    # Get the team name
    teamBasicsList = teamBasics.text.split('\n')
    print(teamBasicsList[0])
    # Get the conference
    conferenceAndRecord = teamBasicsList[1].split('(')
    print(conferenceAndRecord[0])
    # Get the record
    record = conferenceAndRecord[1].split(')')
    print(record[0])

    teamInfoList = websiteInfo.find_all("div", class_="ts-data-center")
    #for teamInfo in teamInfoList:
    #    print(teamInfo.text.strip())
    

# Main script to run the project
if __name__ == '__main__':
    for url in team_urls:
        scrape_net(url)
