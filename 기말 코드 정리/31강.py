# -*- coding: utf-8 -*-
"""
31강: 교차분석(카이제곱검정)
"""


"""
카이제곱검정
"""
import numpy as np
from scipy.stats import chi2_contingency

data = np.array([[43,9],[44,4]])

chi2, p, dof, ex = chi2_contingency(data)
print("Chi-square:", chi2)
print("P-value:", p)
print("Degree of freedom:", dof)

data = np.array([[36,14],[30,25]])

chi2, p, dof, ex = chi2_contingency(data)
print("Chi-square:", chi2)
print("P-value:", p)
print("Degree of freedom:", dof)

"""
Oneway-카이제곱검정
"""
from scipy import stats
obs = [4,6,14,10,16]
stat, p = stats.chisquare(obs)
print("P-value: {0:.4f}".format(p))