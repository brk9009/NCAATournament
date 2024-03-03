import xlsxwriter

class SheetWriter():
    """Write the parsed team's information to a .xlsx file"""

    def __init__(self,contendersData):
        """Initialize the double list contendersData"""
        self.contendersData = contendersData
    
    def write_to_excel(self):
        """Write Information to Excel file"""
        self.create_workbook()
        self.add_formatting()
        self.write_headers()
        self.write_data()

    def create_workbook(self):
        """Create a workbook and add a worksheet"""
        self.workbook = xlsxwriter.Workbook('bracketology.xlsx')
        self.worksheet = self.workbook.add_worksheet('Portfolios')
        # Protect from unwanted edits

    def add_formatting(self):
        """Add formatting to the workbook"""
        # Set the header format
        self.header_format = self.workbook.add_format({
            'bold': True, 'font_name': 'Times New Roman', 'bg_color': 'red', 'font_color': 'yellow'})
        # Set the data format
        self.data_format = self.workbook.add_format({
            'font_name': 'Times New Roman', 'bg_color': 'silver'})

    def write_headers(self):
        """Prepare the headers for the file"""
        # Write the data headers
        self.worksheet.write('A1', 'Team', self.header_format)
        self.worksheet.write('B1', 'Conf.', self.header_format)
        self.worksheet.write('C1', 'Record', self.header_format)
        self.worksheet.write('D1', 'Home Record', self.header_format)
        self.worksheet.write('E1', 'Road Record', self.header_format)
        self.worksheet.write('F1', 'Neutral Record', self.header_format)
        self.worksheet.write('G1', 'SoS', self.header_format)
        self.worksheet.write('H1', 'Non-con SoS', self.header_format)
        self.worksheet.write('I1', 'NET', self.header_format)
        self.worksheet.write('J1', 'KevPauga', self.header_format)
        self.worksheet.write('K1', 'ESPN SoR', self.header_format)
        self.worksheet.write('L1', 'BPI', self.header_format)
        self.worksheet.write('M1', 'KenPom', self.header_format)
        # self.worksheet.write('I1', 'Sagarin', self.header_format)
        self.worksheet.write('N1', 'Quad1', self.header_format)
        self.worksheet.write('O1', 'Quad2', self.header_format)
        self.worksheet.write('P1', 'Quad3', self.header_format)
        self.worksheet.write('Q1', 'Quad4', self.header_format)

    def write_data(self):
        """Write the data from bracketology.py to an excel sheet"""
        # Start from the first cell below the headers
        row = 1
        col = 0
        
        # Loop through the list
        for contenderData in self.contendersData:
            col = 0
            for metric in contenderData:
                self.worksheet.write_string(row, col, metric, self.data_format)
                col += 1

            row +=1

        self.workbook.close()
