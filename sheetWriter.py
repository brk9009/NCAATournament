import xlsxwriter

class SheetWriter():
    """Write the parsed team's information to a .xlsx file"""

    def __init__(self,contendersData):
        """Initialize the double list contendersData"""
        self.contendersData = contendersData
    
    def write_to_excel(self):
        """Write Information to Excel file"""
        self.create_workbook()
        self.write_headers()
        self.write_data()

    def create_workbook(self):
        """Create a workbook and add a worksheet"""
        self.workbook = xlsxwriter.Workbook('bracketology.xlsx')
        self.worksheet = self.workbook.add_worksheet('Portfolios')

    def write_headers(self):
        """Prepare the headers for the file"""
        # Write the data headers
        self.worksheet.write('A1', 'Team')
        self.worksheet.write('B1', 'Conf.')
        self.worksheet.write('C1', 'Record')
        self.worksheet.write('D1', 'NET')
        self.worksheet.write('E1', 'KevPauga')
        self.worksheet.write('F1', 'ESPN SoR')
        self.worksheet.write('G1', 'BPI')
        self.worksheet.write('H1', 'KenPom')
        self.worksheet.write('I1', 'Sagarin')
        self.worksheet.write('J1', 'Quad1')
        self.worksheet.write('K1', 'Quad2')
        self.worksheet.write('L1', 'Quad3')
        self.worksheet.write('M1', 'Quad4')

    def write_data(self):
        """Write the data from bracketology.py to an excel sheet"""
        # Start from the first cell below the headers
        row = 1
        col = 0
        
        # Loop through the list
        for contenderData in self.contendersData:
            col = 0
            for metric in contenderData:
                self.worksheet.write_string(row, col, metric)
                col += 1

            row +=1

        self.workbook.close()
