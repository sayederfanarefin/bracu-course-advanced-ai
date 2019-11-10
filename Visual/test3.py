import xlrd
import numpy as np
import matplotlib.pyplot as plt
file_location = "Book1.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.ncols)]
y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.ncols)]
yerr_pos = [first_sheet.cell_value(i, 2) for i in range(first_sheet.ncols)]
yerr_neg = [first_sheet.cell_value(i, 3) for i in range(first_sheet.ncols)]

yerr = [yerr_neg, yerr_pos]

plt.errorbar(x,y,yerr,fmt='r^')

plt.axis([0,5,0,5])
plt.show()
