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

    def create_workbook(self):
        """Create a workbook and add a worksheet"""
        workbook = xlsxwriter.Workbook('bracketology.xlsx')
        worksheet = workbook.add_worksheet('Portfolios')

    def write_headers(self):
        """Prepare the headers for the file"""
        # Write the data headers
        worksheet.write('A1', 'Team')
        worksheet.write('B1', 'Conf.')
        worksheet.write('C1', 'Record')
        worksheet.write('D1', 'NET')
        worksheet.write('E1', 'NET SoS')
        worksheet.write('F1', 'KevPauga')
        worksheet.write('G1', 'ESPN SoR')
        worksheet.write('H1', 'BPI')
        worksheet.write('I1', 'KenPom')
        worksheet.write('J1', 'Sagarin')
        worksheet.write('K1', 'Quad1')
        worksheet.write('L1', 'Quad2')
        worksheet.write('M1', 'Quad3')
        worksheet.write('N1', 'Quad4')

    def write_data(self):
        """Write the data from bracketology.py to an excel sheet"""
        # Start from the first cell below the headers
        row = 1
        col = 0

        workbook.close()
