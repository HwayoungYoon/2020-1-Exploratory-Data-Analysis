# -*- coding: utf-8 -*-
"""
37강: 선형회귀 - t 통계량, 신뢰구간, 잔차분석(왜도, 첨도)
"""


"""
t 통계량 계산
"""
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.formula.api import ols
from io import StringIO

data_str = '''Region Alcohol Tobacco
North 6.47 4.03
Yorkshire 6.13 3.76
Northeast 6.19 3.77
East_Midlands 4.89 3.34
West_Midlands 5.63 3.47
East_Anglia 4.52 2.92
Southeast 5.89 3.20
Southwest 4.79 2.71
Wales 5.27 3.53
Scotland 6.08 4.51
Northern_Ireland 4.02 4.56'''

df = pd.read_csv(StringIO(data_str), sep=r'\s+')

#회귀분석
lm = ols('Alcohol ~ Tobacco', data = df[:-1]).fit()
print(lm.summary())

#Beta 구하기
i = 1
beta = lm.params[i]

#se 구하기
X = df.Tobacco[:-1]
X = np.vstack((np.ones(X.size), X))
X = np.matrix(X)
C = np.linalg.inv(X*X.T)
C *= lm.mse_resid
SE = np.sqrt(C)
se = SE[i,i]
t = beta/se
print('t =', t)

N = lm.nobs
p = lm.df_model + 1
dof = N - p
p_onesided = 1.0 - stats.t(dof).cdf(t)
p = p_onesided*2.0
print('p = {0:.3f}'.format(p))


"""
신뢰구간(왜도, 첨도)
"""
i = 0

#추정치와 variance
beta, c = lm.params[i], SE[i,i]

#t-통계량의 critical value
N = lm.nobs
P = lm.df_model
dof = N-P-1
z = stats.t(dof).ppf(0.975)

#신뢰구간
print(beta-z*c, beta+z*c)


"""
잔차분석
"""
#Skewness & Kurtosis
Y = df[:-1]["Alcohol"]
d = Y - lm.fittedvalues
S = np.mean(d**3.0)/np.mean(d**2.0)**(3.0/2.0)
K = np.mean(d**4.0)/np.mean(d**2.0)**(4.0/2.0)

print('Skewness: {:.3f}, Kurtosis: {:.3f} '.format(S, K))