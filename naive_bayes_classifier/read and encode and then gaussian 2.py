import pandas as pd
from sklearn.preprocessing import LabelEncoder
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB

total = 140

#get file 
file_location = "Book1.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

#get data from file
sepal_length = [first_sheet.cell_value(i, 1) for i in range(total)]
sepal_width = [first_sheet.cell_value(i, 2) for i in range(total)]

petal_length = [first_sheet.cell_value(i, 3) for i in range(total)]
petal_width = [first_sheet.cell_value(i, 4) for i in range(total)]

species = [first_sheet.cell_value(i, 5) for i in range(total)]

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

default_training_data = np.array([[0, 0,0,0,0]])

i=0
for x in sepal_length_encoded:
    sepal_l = x
    sepal_w = sepal_width_encoded[i]
    petal_l = petal_length_encoded[i]
    petal_w = petal_width_encoded[i]
    spec = species_encoded[i]
    row = np.array([sepal_l, sepal_w, petal_l, petal_w, spec])
    default_training_data = np.vstack((default_training_data, row))
    i=i+1

