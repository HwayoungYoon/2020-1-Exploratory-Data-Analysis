# -*- coding: utf-8 -*-
"""
38강: 선형회귀 - 잔차분석(검정), 이상치
(37강 뒤쪽으로 연결)
"""


"""
잔차분석
"""
#Omnibus 검정
(K2, p) = stats.normaltest(lm.resid)
print('Omnibus: {0:.3f}, p-value = {1:.2f}'.format(K2, p))

#Durbin-Watson
DW = np.sum(np.diff(lm.resid.values)**2.0)/lm.ssr
print('Durbin-Watson: {:.5f}'.format(DW))

#Jaque-Bera Test
JB = (N/6.0)*(S**2.0 + (1.0/4.0)*(K-3.0)**2.0)
p = 1.0 - stats.chi2(2).cdf(JB)
print('JB-statistic: {:.5f}, p-value: {:.5f}'.format(JB, p))

#Condition Number
X = np.matrix(X)
EV = np.linalg.eig(X*X.T)
CN = np.sqrt(EV[0].max()/EV[0].min())
print('Condition No.: {:.5f}'.format(CN))


"""
이상치
"""
lm = ols('Alcohol ~ Tobacco', data = df).fit()
print(lm.summary())