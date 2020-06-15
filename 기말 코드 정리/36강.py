# -*- coding: utf-8 -*-
"""
36강: 선형회귀분석
"""


"""
선형회귀분석
"""
import pandas as pd
import matplotlib.pyplot as plt
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

df = pd.read_csv(StringIO(data_str), sep = r'\s+')

df.plot('Tobacco', 'Alcohol', style = 'o')
plt.ylabel('Alcohol')
plt.title('Sales in Several UK Regions')

lm = ols('Alcohol ~ Tobacco', data = df[:-1]).fit()
print(lm.summary())