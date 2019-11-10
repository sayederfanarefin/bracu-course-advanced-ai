import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Create a test dataframe
df = pd.DataFrame([
       ['green', 1.2, 2017],
       ['blue', 3.1, 2015], 
       ['yellow', 5.6, 2018],
       ['yellow', 5.7, 2018]
])
df.columns = ['color', 'make', 'year']

print(df)

le_color = LabelEncoder()
le_make = LabelEncoder()
df['color_encoded'] = le_color.fit_transform(df.color)
df['make_encoded'] = le_make.fit_transform(df.make)

print(df)
