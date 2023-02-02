import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('eksikveriler.csv') 
# (2)
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy='mean') 

age = data.iloc[:,1:4].values
print(age)
imputer = imputer.fit(age[:,1:4])  # fit() <-- learn 
age[:,1:4] = imputer.transform(age[:,1:4]) # transfrom() <-- transfrom nan to average value
print(age)