import pandas as pd
import random
import numpy as np
import statistics
#Pandas 1
indexes = [1 , 2 , 3 , 4 , 5 , 6]
columns = ['A' , 'B' , 'C' , 'D']
df = pd.DataFrame([[random.random() for j in ['A' , 'B' , 'C' , 'D']] for i in [1 , 2 , 3 , 4 , 5 , 6]], index=indexes,columns=columns)
print(df)
#Pandas 2
print("Two first Rows are:")
print(df.head(2))
print("Two Last Rows are:")
print(df.tail(2))
#Pandas 3
print(df.values)
print(df.columns)
print(df.index)
print(df.describe())
#Pandas 4
df.sort_values(by=['B' , 'C'] , ascending=(False , True) , inplace=True)
print(df)
#Pandas 5
S = pd.Series([0 , 1 , 2 , 3 , 4 , 5 , 6])
print(S)
df['F'] = S
print(df)
#Pandas 6
df.at[[3 , 5] , 'F'] = np.NAN
print(df.loc[[1 , 2 , 3], ['A' , 'F']])
#Pandas 7
df1 = df.dropna()
print(df1)
#Pandas 8
df2 = df.fillna(value=(statistics.mean(df['D'])))
print(df2)