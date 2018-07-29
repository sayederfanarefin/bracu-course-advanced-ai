
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
from sklearn.metrics import confusion_matrix
import math
from sklearn import preprocessing



data = pd.read_csv('Test.csv', header = None, delimiter=' *, *', engine='python')

data.columns = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']

#print(data.isnull().sum())

data_rev = data

le = preprocessing.LabelEncoder()
Sepal_length_cat = le.fit_transform(data.Sepal_length)
Sepal_width_cat = le.fit_transform(data.Sepal_width)
Petal_length_cat   = le.fit_transform(data.Petal_length)
Petal_width_cat = le.fit_transform(data.Petal_width)


data_rev['Sepal_length_cat'] = Sepal_length_cat
data_rev['Sepal_width_cat'] = Sepal_width_cat
data_rev['Petal_length_cat'] = Petal_length_cat
data_rev['Petal_width_cat'] = Petal_width_cat

#print(data_rev)


dummy_fields = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width']
data_rev = data_rev.drop(dummy_fields, axis = 1)

#print(data_rev)

data_rev = data_rev.reindex(['Sepal_length_cat', 'Sepal_width_cat', 'Petal_length_cat', 'Petal_width_cat', 'Species'], axis= 1)
 
data_rev.head(1)



num_features = ['Sepal_length_cat', 'Sepal_width_cat', 'Petal_length_cat', 'Petal_width_cat']
 
scaled_features = {}
for each in num_features:
    mean, std = data_rev[each].mean(), data_rev[each].std()
    scaled_features[each] = [mean, std]
    data_rev.loc[:, each] = (data_rev[each] - mean)/std


features = data_rev.values[:,:4]
target = data_rev.values[:,4]

features_train, features_test, target_train, target_test = train_test_split(features, target, test_size = 0.33, random_state = 2)


clf = GaussianNB()
clf.fit(features_train, target_train)
# target_pred = clf.predict(features_test)








# iris = datasets.load_iris()
# data.shape, iris.target.shape
# ((150, 4), (150,))

# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.33, random_state=10)





# features_train.shape, target_train.shape
# ((90, 4), (90,))
# features_test.shape, target_test.shape
# ((60, 4), (60,))

# classifier = GaussianNB()
# model = classifier.fit(features_train, target_train)
# y = classifier.predict_proba(features_train)
# print (y)

abc = clf.predict(features_test)
print (abc)
print (metrics.accuracy_score(target_test, abc))

sl= LabelEncoder()
r_data= np.array(sl.fit_transform(data.Species))

vpred = cross_val_predict(clf, data, target, cv=5)
print(vpred)
print(metrics.accuracy_score(target, vpred))

x1= metrics.mean_absolute_error(r_data, vpred)
x12= math.sqrt(metrics.mean_absolute_error(r_data, vpred))
x3= math.pow(r2_score(r_data, vpred, multioutput='raw_values'),2)

print(x1)
print(x12)
print(x3)   

metrics.cohen_kappa_score(r_data, vpred, labels=None, weights=None, sample_weight=None)


print(confusion_matrix(r_data, vpred))

