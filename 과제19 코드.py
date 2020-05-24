# -*- coding: utf-8 -*-


#import library
import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy.stats.mstats import kruskalwallis


#data load
df = pd.read_excel("experiment.xls")
group1 = df[df.iloc[:,0]=="Control"]["weight"]
group2 = df[df.iloc[:,0]=="TreatmentA"]["weight"]
group3 = df[df.iloc[:,0]=="TreatmentB"]["weight"]


#levene의 등분산 검정
(W, p) = stats.levene(group1, group2, group3)
if p < 0.05:
    print('Warning: the p-value of the Levene test is <0.05: p=', p)
"""
NO OUTPUT
"""


#일원분산분석
F_statistic, pVal = stats.f_oneway(group1, group2, group3)
print((F_statistic, pVal))
if pVal < 0.05:
    print('One of the groups is significantly different.')
"""
(4.846087862380136, 0.0159099583256229)
One of the groups is significantly different.
"""


#Elegant alternative implementation, with pandas & statsmodels
model = ols('weight ~ C(group)', df).fit()
anovaResults = anova_lm(model)
print(anovaResults)
"""
            df    sum_sq   mean_sq         F   PR(>F)
C(group)   2.0   3.76634  1.883170  4.846088  0.01591
Residual  27.0  10.49209  0.388596       NaN      NaN
"""


#Check if the two results are equal. If they are, there is no output
np.testing.assert_almost_equal(F_statistic, anovaResults['F'][0])
"""
NO OUTPUT
"""


#Kruskal-Wallis 검정
group01 = np.array([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
group02 = np.array([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])
group03 = np.array([6.31,5.12,5.54,5.50,5.37,5.29,4.92,6.15,5.80,5.26])

h, p = kruskalwallis(group01, group02, group03)
print("P value :", p)
if p < 0.05:
    print('There is a significant difference between the group.')
else:
    print('No significant difference between the group.')
"""
P value : 0.018423755731471966
There is a significant difference between the group.
"""

from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""
