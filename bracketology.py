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
            self.get_result_predictive_metrics()
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
        # Get the conference
        conferenceAndRecord = teamBasicsList[1].split('(')
        self.conference = conferenceAndRecord[0]

    def get_result_predictive_metrics(self):
        """Parse through html to get KPI, SOR, BPI, POM, SAG"""
        i = 0

        predictiveMetricsList = self.websiteInfo.find_all("div", class_="ts-data-left")
        # Loop through each 'ts-data-left' data
        for predictiveMetrics in predictiveMetricsList:
            metricsList = predictiveMetrics.text.split('\n')
            if i == 0:
                # KPI is in the 1st spot, sor 2nd
                self.kpi = metricsList[1].lstrip(' ')
                self.sor = metricsList[2].lstrip(' ')
            elif i == 1:
                # BPI 1st, ken pom 2nd, sagarin 3rd
                self.bpi = metricsList[1].lstrip(' ')
                self.pom = metricsList[2].lstrip(' ')
                # Sagarin is outdated
                # self.sag = metricsList[3].lstrip(' ')
            i=i+1

    def get_other_metrics(self):
        """Parse through html to get NET, record, NET SoS, etc."""
        i = 0

        otherMetricsList = self.websiteInfo.find_all("div", class_="ts-data-center")
        # Loop through each 'ts-data-center' data
        for otherMetrics in otherMetricsList:
            metricsList = otherMetrics.text.split('\n')
            # first 'ts-data-center' is NET
            if i == 0:
                # Relevant data is in the 3rd spot
                self.net = metricsList[2].lstrip(' ')
            elif i == 3:
                self.sos = metricsList[1].lstrip(' ')
                self.nonconSos = metricsList[2].lstrip(' ')
            elif i == 6:
                self.q1 = metricsList[2].lstrip(' ')
            elif i == 7:
                self.q2 = metricsList[2].lstrip(' ')
            elif i == 8:
                self.q3 = metricsList[2].lstrip(' ')
            elif i == 9:
                self.q4 = metricsList[2].lstrip(' ')
            elif i == 10:
                self.record = metricsList[2].lstrip(' ')
                self.homeRecord = metricsList[3].lstrip(' ')
                self.roadRecord = metricsList[4].lstrip(' ')
                self.neutralRecord = metricsList[5].lstrip(' ')
            i=i+1


    def add_team_metrics_to_list(self):
        """Add the team's metrics to their own list."""
        self.individualTeamData.append(self.teamName.strip())
        self.individualTeamData.append(self.conference.strip())
        self.individualTeamData.append(self.record.strip())
        self.individualTeamData.append(self.homeRecord.strip())
        self.individualTeamData.append(self.roadRecord.strip())
        self.individualTeamData.append(self.neutralRecord.strip())
        self.individualTeamData.append(self.sos.strip())
        self.individualTeamData.append(self.nonconSos.strip())
        self.individualTeamData.append(self.net.strip())
        self.individualTeamData.append(self.kpi.strip())
        self.individualTeamData.append(self.sor.strip())
        self.individualTeamData.append(self.bpi.strip())
        self.individualTeamData.append(self.pom.strip())
        #self.individualTeamData.append(self.sag.strip())
        self.individualTeamData.append(self.q1.strip())
        self.individualTeamData.append(self.q2.strip())
        self.individualTeamData.append(self.q3.strip())
        self.individualTeamData.append(self.q4.strip())

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
