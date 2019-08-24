import numpy as np
import pandas as pd
data=pd.read_csv('media/order/demo.csv',encoding='gbk')
data1=pd.get_dummies(data[['专业程度','学历']])
data2=data1.drop(['专业程度_非专业','学历_专科'],axis=1)
data3=pd.concat([data2,data[['人数','校外','重要程度']]],axis=1)
# print(data)
# print(data3)
x=data3.iloc[:,:-1]
y=data3.iloc[:,-1:]
from sklearn.linear_model import LinearRegression
model=LinearRegression().fit(x,y)




