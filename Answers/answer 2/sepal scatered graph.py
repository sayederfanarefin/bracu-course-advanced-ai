import xlrd
import numpy as np
import matplotlib.pyplot as plt
file_location = "Book1.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

x1 = [first_sheet.cell_value(i, 1) for i in range(50)]
y1 = [first_sheet.cell_value(i, 2) for i in range(50)]

x2 = [first_sheet.cell_value(i, 1) for i in range(51, 100)]
y2 = [first_sheet.cell_value(i, 2) for i in range(51, 100)]

x3 = [first_sheet.cell_value(i, 1) for i in range(101, 150)]
y3 = [first_sheet.cell_value(i, 2) for i in range(101, 150)]

colors1 = (1,0,0)
colors2 = (0,0,1)
colors3 = (0,1,0)
area = np.pi*3
 
# Plot
plt.scatter(x1, y1, s=area, c=colors1, alpha=0.9)
plt.scatter(x2, y2, s=area, c=colors2, alpha=0.9)
plt.scatter(x3, y3, s=area, c=colors3, alpha=0.9)
plt.title('Mid term')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
a
