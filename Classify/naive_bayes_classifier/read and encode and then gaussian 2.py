import pandas as pd
from sklearn.preprocessing import LabelEncoder
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB

train_total = 140
target_total = 10

#get file 
file_location = "Book1.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

#get data from file
sepal_length = [first_sheet.cell_value(i, 1) for i in range(train_total)]
sepal_width = [first_sheet.cell_value(i, 2) for i in range(train_total)]

petal_length = [first_sheet.cell_value(i, 3) for i in range(train_total)]
petal_width = [first_sheet.cell_value(i, 4) for i in range(train_total)]

species = [first_sheet.cell_value(i, 5) for i in range(train_total)]

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

#data prep for naive guy
#training data
default_training_data = np.array([[0, 0,0,0]])

i=0
for x in sepal_length_encoded:
    sepal_l = x
    sepal_w = sepal_width_encoded[i]
    petal_l = petal_length_encoded[i]
    petal_w = petal_width_encoded[i]
   
    row = np.array([sepal_l, sepal_w, petal_l, petal_w])
    if(i==0):
        default_training_data = row
    else:
        default_training_data = np.vstack((default_training_data, row))
    i=i+1
    
print("printing default training data: =>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>")
print(default_training_data)

#training lables
default_training_labels = np.array(species_encoded)
print("printing default training lables: =>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>")
print(default_training_labels)



#target
default_target = np.array([[0, 0,0,0]])


#get data from file
sepal_length2 = [first_sheet.cell_value(i, 1) for i in range(train_total, train_total+target_total)]
sepal_width2 = [first_sheet.cell_value(i, 2) for i in range(train_total, train_total+target_total)]

petal_length2 = [first_sheet.cell_value(i, 3) for i in range(train_total, train_total+target_total)]
petal_width2 = [first_sheet.cell_value(i, 4) for i in range(train_total, train_total+target_total)]

species2 = [first_sheet.cell_value(i, 5) for i in range(train_total, train_total+target_total)]


#define encoder
sepal_length_encoder2 = LabelEncoder()
sepal_width_encoder2 = LabelEncoder()

petal_length_encoder2 = LabelEncoder()
petal_width_encoder2 = LabelEncoder()

species_encoder2 = LabelEncoder()

#encoded values
sepal_length_encoded2 = sepal_length_encoder2.fit_transform(sepal_length2)
sepal_width_encoded2 = sepal_width_encoder2.fit_transform(sepal_width2)

petal_length_encoded2 = petal_length_encoder2.fit_transform(petal_length2)
petal_width_encoded2 = petal_width_encoder2.fit_transform(petal_width2)

species_encoded2 = species_encoder2.fit_transform(species2)
print("result expected")
print(species_encoded2)

#data prep for naive guy
#target data
default_target = np.array([[0, 0,0,0]])

i2=0
for x2 in sepal_length_encoded2:
    sepal_l2= x2
    sepal_w2 = sepal_width_encoded2[i2]
    petal_l2 = petal_length_encoded2[i2]
    petal_w2 = petal_width_encoded2[i2]
   
    row2 = np.array([sepal_l2, sepal_w2, petal_l2, petal_w2])
    if(i2==0):
        default_target = row2
    else:
        default_target = np.vstack((default_target, row2))
    i2=i2+1

print("printing default target data: =>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>")
print(default_target)


class NaiveBayesClassifier:
    

    def __init__(self):
        self.y_pred = None
        self.clf = GaussianNB()
        

    def print_results(self):
        for item in range(len(self.y_pred)):
            print("Predict: {:d}".format(self.y_pred[item]))

    def fit(self, data=default_training_data, labels=default_training_labels):
        self.clf.fit(data, labels)
        return self

    def predict(self, target=default_target):
        self.y_pred = self.clf.predict(target)
        return self


if __name__ == "__main__":
    tc = NaiveBayesClassifier()
    tc.fit()
    tc.predict()
    tc.print_results()








