# -*- coding: utf-8 -*-

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
Tval = (110-np.mean(y))/np.sqrt(np.var(y)/float(len(y)))

#분포표 구하기
td = stats.t(len(y)-1)

#분포표에서 P-value 구하기
P = td.sf(Tval)

#T값과 P값 프린트
print('t-statistic = %6.4f p-value = %6.4f' % (Tval, P))
"""
t-statistic = 1.9353 p-value = 0.0425
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 141991317885390
"""