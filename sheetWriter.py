import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('bracketology.xlsx')
worksheet = workbook.add_worksheet('Portfolios')

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




workbook.close()
