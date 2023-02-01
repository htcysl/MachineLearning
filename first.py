import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('veriler.csv') 
print(data)

Height_weight = data[['boy','kilo']]
#print(Height_weight) 


# class 
class Person :
    height = 180 
    def run(self,b):
      return b+10

p = Person() 
print(p.height)
print(p.run(10)) 


 



