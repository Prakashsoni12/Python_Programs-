import numpy as np
import pandas as pd

pdata = pd.read_csv('matches - matches.csv')
print(pdata)
print(pdata.head(2))#bydefault head() gives 5 values at time. but you can change it by passing n number of arguments
print('-------------------------')
print(pdata.tail())#bydefault tail() gives 5 values at time. but you can change it by passing n number of arguments
print(pdata.shape)
print(pdata.info())
print(pdata.describe())#it provides high level mathmaticle summry of data
print(pdata['winner'])#you can directly fetch any columns of data
print(pdata.iloc[1:3])#you can perform slicing operation over datafreames(generally this iloc function fetches rows of table)
print(pdata.iloc[:,[4,5,10]])#here you can also fetch columns with rows