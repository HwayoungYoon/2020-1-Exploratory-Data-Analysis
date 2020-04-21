# -*- coding: utf-8 -*-

#단순선형회귀_아버지와 아들의 키
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.array([135,155,175,186,192,202,205,160,170])
y = np.array([140,160,170,180,199,189,200,170,168])
model = stats.linregress(x,y)
print(model)
"""
LinregressResult(slope=0.793343011198673, intercept=35.83533803401076, rvalue=0.9529171371055305, pvalue=7.120454332493714e-05, stderr=0.0954179721097493)
"""

plt.plot(x,y,'o',color='black')
plt.xlabel("father's height")
plt.ylabel("son's height")
plt.axis([100,250,100,250])
plt.plot(x, x*model.slope + model.intercept, 'b')
plt.title("Linear regression for Father and Son")
plt.savefig('lr_fa&son.png', bbox_inches='tight')


#단순선형회귀_인터넷에서 데이터 가져오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("http://www.jaredlander.com/data/housing.csv")
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2626 entries, 0 to 2625
Data columns (total 13 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Neighborhood             2626 non-null   object 
 1   Building.Classification  2626 non-null   object 
 2   Total.Units              2626 non-null   int64  
 3   Year.Built               2530 non-null   float64
 4   Gross.SqFt               2626 non-null   int64  
 5   Estimated.Gross.Income   2626 non-null   int64  
 6   Gross.Income.per.SqFt    2626 non-null   float64
 7   Estimated.Expense        2626 non-null   int64  
 8   Expense.per.SqFt         2626 non-null   float64
 9   Net.Operating.Income     2626 non-null   int64  
 10  Full.Market.Value        2626 non-null   int64  
 11  Market.Value.per.SqFt    2626 non-null   float64
 12  Boro                     2626 non-null   object 
dtypes: float64(4), int64(6), object(3)
memory usage: 236.0+ KB
"""

x = df["Total.Units"]
y = df["Market.Value.per.SqFt"]
reg = linear_model.LinearRegression()

reg.fit(x.values.reshape(-1,1), y)
"""
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
"""

plt.plot(x, y, 'o')
plt.plot(x, reg.predict(x.values.reshape(-1,1)))
plt.savefig('lr_housing.png', bbox_inches='tight')


#reshape in numpy
z = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
z.shape
"""
(3, 4)
"""
z.reshape(-1)
"""
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
"""
z.reshape(-1,1)
"""
array([[ 1],
       [ 2],
       [ 3],
       [ 4],
       [ 5],
       [ 6],
       [ 7],
       [ 8],
       [ 9],
       [10],
       [11],
       [12]])
"""
