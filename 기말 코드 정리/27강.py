# -*- coding: utf-8 -*-
"""
27강: 제 1종 오류, 제 2종 오류, 표본 수 계산, 검정과 모델링
"""


"""
alpha와 beta를 고려한 표본 수 계산
"""
from statsmodels.stats import power

nobs = power.tt_ind_solve_power(effect_size = 0.5, alpha = 0.05, power = 0.8)
print(nobs)


"""
검정과 모델링 - 두 평균의 차이
"""
import numpy as np
from scipy import stats

#Generate the data
np.random.seed(123)
race_1 = np.round(np.random.randn(20)*10+90)
race_2 = np.round(np.random.randn(20)*10+85)

#t-test
(t, pVal) = stats.ttest_rel(race_1, race_2)

#Show the result
print('The probability that the two distributions are equal is {0:5.3f} .'.format(pVal))


"""
검정과 모델링 - 차이의 추정
"""
import pandas as pd
import statsmodels.formula.api as sm
import numpy as np

np.random.seed(123)

race_1 = [79,100,93,75,84,107,66,86,103,81,83,89,105,84,86,86,112,112,100,94]
race_2 = [92,100,76,97,72,79,94,71,84,76,82,57,67,78,94,83,85,92,76,88]

df = pd.DataFrame({'Race1': race_1, 'Race2': race_2})
result = sm.ols(formula = 'I(Race2-Race1) ~ 1', data = df).fit()
print(result.summary())