# -*- coding: utf-8 -*-
"""
24강: 정규성 검정, 가설 검정
"""


"""
정규성 검정
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

#파라미터 N(0,3^2) 생성
myMean = 0
mySD = 3

#초기값
np.random.seed(1234)

#정규 난수 생성
data = stats.norm.rvs(myMean, mySD, 1000)
plt.hist(data)

stats.probplot(data, plot=plt)
stats.normaltest(data)

#omnibus test
pVals = pd.Series()
_, pVals['Omnibus'] = stats.normaltest(data)

if pVals['Omnibus'] > 0.5:
    print("Data are normally distributed")

#chissquareN(df=2) 생성 후 normality test
data2 = np.random.chisquare(2, 1000)
stats.probplot(data2, plot=plt)
stats.normaltest(data2)

pVals = pd.Series()
_, pVals['Omnibus'] = stats.normaltest(data2)

print('P-values for all {0} data points:'.format(len(data2)))
print(pVals)

if pVals['Omnibus'] < 0.5:
    print("Data are not normally distributed")


"""
가설 검정
"""
#import library
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#x, y 값 지정
y = np.array([109.4, 76.2, 128.7, 93.7, 85.6, 117.7, 117.2, 87.3, 100.3, 55.1])
x = list(range(10))

#분포 확인을 위한 플롯 생성
scatter = plt.scatter(x,y)
plt.axhline(y=100, color='r', linestyle='-')
plt.xlim = (x[0]-1, x[-1]+1)
plt.ylim = (np.min(y-1), np.max(y+1))
plt.xlabel('Student Number')
plt.ylabel('Score')

#평균에 대한 t-통계량
Tval = (100-np.mean(y))/np.sqrt(np.var(y)/float(len(y)))

#분포표 구하기
td = stats.t(len(y)-1)

#분포표에서 P-value 구하기
P = td.sf(Tval)

#T값과 P값 프린트
print('t-statistic = %6.4f p-value = %6.4f' % (Tval, P))