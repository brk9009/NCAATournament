import requests
from bs4 import BeautifulSoup

from teams import teamUrls
from sheetWriter import SheetWriter

#urls = ["https://www.warrennolan.com/basketball/2022/team-net-sheet?team=Bellarmine"]

class NetSheetParser():
    """Parse the net sheet for bracketology"""
    global contendersData
    contendersData = list()

    def __init__(self, teamUrls):
        """Initialize the urls"""
        self.teamUrls = teamUrls

    def get_every_teams_data(self):
        """Go through all the teams that can make the tournament"""
        for url in self.teamUrls:
            self.get_website_info(url)
        # After looping, return every team's data    
        return contendersData

    def get_website_info(self, url):
        """Get the team's html to parse through"""
        # Get the HTML data
        page = requests.get(url)

        # print(page.text)
        # Create a BeautifulSoup object that uses the html parser to parse the page.
        soup = BeautifulSoup(page.content, "html.parser")

        # Find the team's information from the "container-x" id
        self.websiteInfo = soup.find(id="container-x")
        #print(websiteInfo.prettify())

        self.get_name_conf_record()

    def get_name_conf_record(self):
        """Parse through html to get the team's metrics"""
        self.teamInfoList = []

        # Parse the team name, conference, and record
        teamBasics = self.websiteInfo.find("div", class_="ts-teamname")
        # Get the team name
        teamBasicsList = teamBasics.text.split('\n')
        print(teamBasicsList[0])
        # Get the conference
        conferenceAndRecord = teamBasicsList[1].split('(')
        print(conferenceAndRecord[0])
        # Get the record
        record = conferenceAndRecord[1].split(')')
        print(record[0])

        self.teamInfoList.append(teamBasicsList[0].strip())
        self.teamInfoList.append(conferenceAndRecord[0].strip())
        self.teamInfoList.append(record[0].strip())
        #print(self.teamInfoList)

        #teamInfoList = self.websiteInfo.find_all("div", class_="ts-data-center")
        #for teamInfo in teamInfoList:
        #    print(teamInfo.text.strip())

        self.add_team_metrics_to_global_list()
    
    def add_team_metrics_to_global_list(self):
        """Add the team's metrics to a list with every team's metrics"""
        contendersData.append(self.teamInfoList)
        #print(contendersData)

# Main script to run the project
netSheetParser = NetSheetParser(teamUrls)
teamSheets = netSheetParser.get_every_teams_data()
print(teamSheets)
