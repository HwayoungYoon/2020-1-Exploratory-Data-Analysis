# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy.stats.mstats import kruskalwallis

df = pd.read_excel("experiment.xls")

group1 = df[df.iloc[:,1]==1][0]
group2 = df[df.iloc[:,1]==2][0]
group3 = df[df.iloc[:,1]==3][0]

#levene의 등분산 검정
(W, p) = stats.levene(group1, group2, group3)
if p < 0.05:
    print('Warning: the p-value of the Levene test is <0.05: p=', p)

#일원분산분석
F_statistic, pVal = stats.f_oneway(group1, group2, group3)
print((F_statistic, pVal))
if pVal < 0.05:
    print('One of the groups is significantly different.')

#Elegant alternative implementation, with pandas & statsmodels
model = ols('weight ~ C(group)', df).fit()
anovaResults = anova_lm(model)
print(anovaResults)

#Check if the two results are equal. If they are, there is no output
np.testing.assert_almost_equal(F_statistic, anovaResults['F'][0])

#Kruskal-Wallis 검정
h, p = kruskalwallis(group1, group2, group3)
print("P value :", p)
if p < 0.05:
    print('There is a significant difference between the group.')
else:
    print('No significant difference between the group.')





