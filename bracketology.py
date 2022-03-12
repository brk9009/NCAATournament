import requests
from bs4 import BeautifulSoup

from teams import teamUrls
from sheetWriter import SheetWriter

class NetSheetParser():
    """Parse the net sheet for bracketology"""

    def __init__(self, teamUrls):
        """Initialize the urls"""
        self.teamUrls = teamUrls
        self.allContendersData = list()

    def get_every_teams_data(self):
        """Go through all the teams that can make the tournament"""
        for url in self.teamUrls:
            self.get_website_html(url)
            self.get_name_conf()
            self.get_other_metrics()
            self.add_team_metrics_to_list()
            self.add_team_metrics_to_global_list()
        # After looping, return every team's data    
        return self.allContendersData

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
        self.individualTeamData = []

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
        i = 0

        otherMetricsList = self.websiteInfo.find_all("div", class_="ts-data-center")
        # Loop through each 'ts-data-center' data
        for otherMetrics in otherMetricsList:
            metricsList = otherMetrics.text.split('\n')
            # first 'ts'data'center' is NET
            if i == 0:
                # Relevant data is in the 3rd spot
                self.net = metricsList[2].lstrip(' ')
                print(self.net)
            elif i == 1:
                self.record = metricsList[2].lstrip(' ')
                print(self.record)
            i=i+1


    def add_team_metrics_to_list(self):
        """Add the team's metrics to their own list."""
        self.individualTeamData.append(self.teamName.strip())
        self.individualTeamData.append(self.conference.strip())
        self.individualTeamData.append(self.record.strip())
        self.individualTeamData.append(self.net.strip())
        print(self.individualTeamData)

    def add_team_metrics_to_global_list(self):
        """Add the team's metric list to a list with every team's metrics"""
        self.allContendersData.append(self.individualTeamData)
        #print(contendersData)

# Main script to run the project
netSheetParser = NetSheetParser(teamUrls)
teamSheets = netSheetParser.get_every_teams_data()
#print(teamSheets)
sheetWriter = SheetWriter(teamSheets)
sheetWriter.write_to_excel()
