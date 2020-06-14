# -*- coding: utf-8 -*-
"""
32강: 신뢰구간, 교차분석(피셔의 정확검정)
"""


"""
신뢰구간
"""
import numpy as np

p = 10/100000
n = 2500
lower = n*p - 1.96*np.sqrt(n*p*(1-p))
upper = n*p + 1.96*np.sqrt(n*p*(1-p))

print("The 95% confidence interval for the incidence of breast cancer is from {0:.1f} to {1:.1f}".format(lower, upper))

p = 3.8/100
n = 2500
lower = n*p - 1.96*np.sqrt(n*p*(1-p))
upper = n*p + 1.96*np.sqrt(n*p*(1-p))

print("The 95% confidence interval for the incidence of breast cancer is from {0:.0f} to {1:.0f}".format(lower, upper))


"""
피셔의 정확검정
"""
import numpy as np
from scipy.stats import fisher_exact

data = np.array([[4,2],[1,3]])
oddsratio, pValue = fisher_exact(data)
print("P-value:", pValue)

data = np.array([[3,1],[1,3]])
oddsratio, pValue = fisher_exact(data, alternative = 'greater')
print("P-value: {0:.4f}".format(pValue))