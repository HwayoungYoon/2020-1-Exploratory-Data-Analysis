# -*- coding: utf-8 -*-
"""
33강: 교차분석(맥니마검정)
"""


"""
맥니마검정
"""
from statsmodels.stats.contingency_tables import mcnemar

obs = [[510,16], [5,90]]

result = mcnemar(obs)

print('statistic = %d, p-value = %.3f' % (result.statistic, result.pvalue))