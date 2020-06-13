# -*- coding: utf-8 -*-
"""
29강: 비모수검정(Kruskal-Wallis 검정), 이원분산분석
"""


"""
Kruskal-Wallis 검정
"""
import numpy as np
from scipy.stats.mstats import kruskalwallis

#These data could be a comparison of the smog level in four different cities.
city1 = np.array([68,93,123,83,108,122])
city2 = np.array([119,116,101,103,113,84])
city3 = np.array([70,68,54,73,81,68])
city4 = np.array([61,54,59,67,59,70])

h, p = kruskalwallis(city1, city2, city3, city4)

print("P value :", p)
if p < 0.05:
    print('There is a significant difference between the group.')
else:
    print('No significant difference between the group.')


"""
이원분산분석
"""
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = pd.read_csv("altman_12_6.txt", header=None)
df.columns = ["hs", "fetus", "observer"]

formula = 'hs ~ C(fetus) + C(observer) + C(fetus):C(observer)'
lm = ols(formula, df).fit()
anovaResults = anova_lm(lm)
print(anovaResults)