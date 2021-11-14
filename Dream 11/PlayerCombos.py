# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')


count = int(input())
player_list = [input() for i in range(count)]
serial = 1
for i in range(count):
	for j in range(count):
		if j != i:
			print(serial, player_list[i], player_list[j], sep='\t')
			sheet1.write(serial, 0, player_list[i])
			sheet1.write(serial, 1, player_list[j])
			serial += 1

wb.save('D:\Programming\Python\Github\Python_General\Dream 11\player test.xls')
