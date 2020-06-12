# -*- coding: utf-8 -*-

#import library
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.formula.api import ols
from io import StringIO


#data
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

#데이터 분포 plot
df.plot('Tobacco', 'Alcohol', style='o')
plt.ylabel('Alcohol')
plt.xlabel('Sales in Several UK Regions')

#회귀분석
lm = ols('Alcohol ~ Tobacco', data = df[:-1]).fit()

#Omnibus 검정
(K2, p) = stats.normaltest(lm.resid)
print('Omnibus: {0:.3f}, p = {1:.2f}'.format(K2, p))
"""
Omnibus: 2.542, p = 0.28
C:\Python\anaconda3\lib\site-packages\scipy\stats\stats.py:1535: UserWarning: kurtosistest only valid for n>=20 ... continuing anyway, n=10
  "anyway, n=%i" % int(n))
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""