



import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import naive_bayes
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_predict
from sklearn import datasets
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import math


data = pd.read_csv('Test.csv')
iris = datasets.load_iris()
data.shape, iris.target.shape
((150, 4), (150,))

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, random_state=0)

X_train.shape, y_train.shape
((90, 4), (90,))
X_test.shape, y_test.shape
((60, 4), (60,))

classifier = GaussianNB()
model = classifier.fit(X_train, y_train)
y = classifier.predict_proba(X_train)
print (y)

abc = classifier.predict(X_test)
print (y_test)
print (abc)
print (metrics.accuracy_score(y_test, abc))

sl= LabelEncoder()
rawdata= np.array(sl.fit_transform(data.Species))
print(rawdata)

cvprd = cross_val_predict(classifier, iris.data, iris.target, cv=5)
print(cvprd)
print(metrics.accuracy_score(iris.target, cvprd))




x1= metrics.mean_absolute_error(rawdata, cvprd)
x12= math.sqrt(metrics.mean_absolute_error(rawdata, cvprd))
x3= math.pow(r2_score(rawdata, cvprd, multioutput='raw_values'),2)

print(x1)
print(x12)
print(x3)   

metrics.cohen_kappa_score(rawdata, cvprd, labels=None, weights=None, sample_weight=None)

from sklearn.metrics import confusion_matrix

confusion_matrix(rawdata, cvprd)

