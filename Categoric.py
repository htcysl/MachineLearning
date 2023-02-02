import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# (3)
data = pd.read_csv('veriler.csv') 
#print(data)


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy='mean') 

age = data.iloc[:,1:4].values
#print(age)
imputer = imputer.fit(age[:,1:4])  # fit() <-- learn 
age[:,1:4] = imputer.transform(age[:,1:4]) # transfrom() <-- transfrom nan to average value
#print(age)


country = data.iloc[:,0:1].values
#print(country) 


# encode categoric to numeric values 
from sklearn import preprocessing

le = preprocessing.LabelEncoder() 

country[:,0] = le.fit_transform(data.iloc[:,0])
#print(country)

ohe = preprocessing.OneHotEncoder()
country = ohe.fit_transform(country).toarray()
#print(country) 
 
result = pd.DataFrame(data=country,index=range(22),columns=['fr','tr','us']) 
#print(result)

result2 = pd.DataFrame(data=age,index=range(22),columns=['height','weight','age'])
#print(result2)

gender = data.iloc[:,-1].values
#print(gender)

result3 = pd.DataFrame(data=gender,index=range(22),columns=['gender'])
#print(result3)

r1 =  pd.concat([result,result2],axis = 1)
#print(r1)

r2 = pd.concat([r1,result3],axis=1)
#print(r2)

# divide the data set
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(r1,result3,test_size=0.33,random_state=0)
#print("x train data set :")
#print(x_train )

#print("x test data set :")
#print(x_test)

#print("y train data set : ")
#print(y_train)

#print("y test data set :")
#print(y_test)

# normalize 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler() 
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test) 

print(X_train)
print("--------------------")
print(X_test)





