import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('veriler.csv')
#print(data) 

#encoder (for county) : categoric to numeric 
country = data.iloc[:,0:1].values

from sklearn import preprocessing 
le = preprocessing.LabelEncoder() 
country[:,0] = le.fit_transform(data.iloc[:,0]) 

ohe = preprocessing.OneHotEncoder() 
country = ohe.fit_transform(country).toarray() 

#encoder(for gender) : categoric to numeric 
gender = data.iloc[:,-1:].values 
gender[:,-1] = le.fit_transform(data.iloc[:,-1])

gender = ohe.fit_transform(gender).toarray() 
print(gender)
