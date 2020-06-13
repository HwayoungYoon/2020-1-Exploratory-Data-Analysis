# -*- coding: utf-8 -*-
"""
28강: 제 1종 오류, 제 2종 오류, 평균검정, 분산분석(일원분산분석), 사후검정
"""


"""
일원분산분석
"""
import numpy as np
from scipy import stats
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

data = pd.read_csv("altman_910.txt", header=None)
data.columns = ['value', 'treatment']

group1 = data[data.iloc[:,1] == 1]["value"]
group2 = data[data.iloc[:,1] == 2]["value"]
group3 = data[data.iloc[:,1] == 3]["value"]

#levene의 등분산 검정
(W, p) = stats.levene(group1, group2, group3)
if p < 0.05:
    print('Warning: the P-value of the Levene test is <0.05: p=', p)

#One-way ANOVA
F_statistic, pVal = stats.f_oneway(group1, group2, group3)
print((F_statistic, pVal))

if pVal < 0.05:
    print('One of the groups is significantly different.')

#Elegant alternative implementation, with pandas & statsmodels
model = ols('value ~ C(treatment)', data).fit()
anovaResults = anova_lm(model)
print(anovaResults)

#Check if the two results are equal. If they are, there is no output
np.testing.assert_almost_equal(F_statistic, anovaResults['F'][0])


"""
사후검정
"""
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

plot_data = [group1, group2, group3]
ax = plt.boxplot(plot_data)

df = pd.DataFrame(data, columns = ["value", "treatment"])
posthoc = pairwise_tukeyhsd(df['value'], df['treatment'], alpha = 0.05)
print(posthoc)

fig = posthoc.plot_simultaneous()