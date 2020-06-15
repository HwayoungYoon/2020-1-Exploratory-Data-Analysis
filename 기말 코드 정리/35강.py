# -*- coding: utf-8 -*-
"""
35강: 선형회귀분석
"""


"""
선형회귀분석
"""
import pandas as pd
from statsmodels.formula.api import ols

data = pd.read_csv("altman_11_1.txt", header=None)
data.columns = ['vcf', 'glucose']

y = data.vcf
x = data.glucose

lm = ols('y ~ x', data = data).fit()
print(lm.summary())

import pandas as pd
import numpy as np

x = np.array([15.3,10.8,8.1,19.5,7.2,5.3,9.3,11.1,7.5,12.2,6.7,5.2,19.0,15.1,6.7,4.2,10.3,12.5,16.1,13.3,4.9,8.8,9.5])
y = np.array([1.76,1.34,1.27,1.47,1.27,1.49,1.31,1.09,1.18,1.22,1.25,1.19,1.95,1.28,1.52,1.12,1.37,1.19,1.05,1.32,1.03,1.12,1.70])

# y = a + bx 의 a와 b 계산
n = len(x) # number of samples
Sxx = np.sum(x**2) - np.sum(x)**2/n
Sxy = np.sum(x*y) - np.sum(x)*np.sum(y)/n

mean_x = np.mean(x)
mean_y = np.mean(y)

b = Sxy/Sxx
a = mean_y - b*mean_x

print('y = {0:.4f} + {1:.4f}x'.format(a, b))