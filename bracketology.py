import requests
from bs4 import BeautifulSoup

from teams import teamUrls
from sheetWriter import SheetWriter

class NetSheetParser():
    """Parse the net sheet for bracketology"""

    def __init__(self, teamUrls):
        """Initialize the urls"""
        self.teamUrls = teamUrls
        self.contendersData = list()

    def get_every_teams_data(self):
        """Go through all the teams that can make the tournament"""
        for url in self.teamUrls:
            self.get_website_html(url)
            self.get_name_conf()
            self.get_other_metrics()
            self.add_team_metrics_to_list()
            #self.add_team_metrics_to_global_list()
        # After looping, return every team's data    
        return self.contendersData

    def get_website_html(self, url):
        """Get the team's html to parse through"""
        # Get the HTML data
        page = requests.get(url)
        # print(page.text)

        # Create a BeautifulSoup object that uses the html parser to parse the page.
        soup = BeautifulSoup(page.content, "html.parser")

        # Find the team's information from the "container-x" id
        self.websiteInfo = soup.find(id="container-x")
        #print(websiteInfo.prettify())

    def get_name_conf(self):
        """Parse through html to get the team's name and conference"""
        self.teamInfoList = []

        # Parse the team name and conference
        teamBasics = self.websiteInfo.find("div", class_="ts-teamname")
        # Get the team name
        teamBasicsList = teamBasics.text.split('\n')
        self.teamName = teamBasicsList[0]
        print(self.teamName)
        # Get the conference
        conferenceAndRecord = teamBasicsList[1].split('(')
        self.conference = conferenceAndRecord[0]
        print(self.conference)

    def get_other_metrics(self):
        """Parse through html to get NET, record, NET SoS, etc."""
        teamInfoList = self.websiteInfo.find_all("div", class_="ts-data-center")
        for teamInfo in teamInfoList:
            print(teamInfo.text.strip())

    def add_team_metrics_to_list(self):
        """Add the team's metrics to their own list."""
        self.teamInfoList.append(self.teamName.strip())
        self.teamInfoList.append(self.conference.strip())
        print(self.teamInfoList)

    def add_team_metrics_to_global_list(self):
        """Add the team's metric list to a list with every team's metrics"""
        self.contendersData.append(self.teamInfoList)
        #print(contendersData)

# Main script to run the project
netSheetParser = NetSheetParser(teamUrls)
teamSheets = netSheetParser.get_every_teams_data()
#print(teamSheets)
sheetWriter = SheetWriter(teamSheets)
sheetWriter.write_to_excel()
