import pandas as pd
from sklearn.preprocessing import LabelEncoder
import xlrd
import numpy as np
import matplotlib.pyplot as plt

#get file 
file_location = "Book1.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

#get data from file
sepal_length = [first_sheet.cell_value(i, 1) for i in range(150)]
sepal_width = [first_sheet.cell_value(i, 2) for i in range(150)]

petal_length = [first_sheet.cell_value(i, 3) for i in range(150)]
petal_width = [first_sheet.cell_value(i, 4) for i in range(150)]

species = [first_sheet.cell_value(i, 5) for i in range(150)]

#define encoder
sepal_length_encoder = LabelEncoder()
sepal_width_encoder = LabelEncoder()

petal_length_encoder = LabelEncoder()
petal_width_encoder = LabelEncoder()

species_encoder = LabelEncoder()

#encoded values
sepal_length_encoded = sepal_length_encoder.fit_transform(sepal_length)
sepal_width_encoded = sepal_width_encoder.fit_transform(sepal_width)

petal_length_encoded = petal_length_encoder.fit_transform(petal_length)
petal_width_encoded = petal_width_encoder.fit_transform(petal_width)

species_encoded = species_encoder.fit_transform(species)


#print
print(species_encoded)
