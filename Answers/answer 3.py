import pandas as pd
data = pd.read_csv('Test.csv')
print("Mean")
print(data.mean())
print("Standard Deviation")
print(data.std())
print(data.describe())
group= data.groupby('Species')
print(group.describe())

