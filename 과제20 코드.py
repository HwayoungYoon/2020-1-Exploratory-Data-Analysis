# -*- coding: utf-8 -*-


#import library
import numpy as np
from scipy import stats


#data 입력
group1 = np.array([76,101,66,72,88,82,79,73,76,85,75,64,76,81,86])
group2 = np.array([64,65,56,62,59,76,66,82,91,57,92,80,82,67,54])


#통계량 계산
t_statistic, pVal = stats.ttest_ind(group1, group2)
u, p_value = stats.mannwhitneyu(group1, group2)


#independent t-test
print("T-stat: {0:.4f}, P-value: {1:.4f}".format(t_statistic, pVal))
"""
T-stat: 2.0969, P-value: 0.0452
"""


#Mann-Whitney t-test
print("Mann-Whitney test U-statistic: {0:.4f}".format(u))
print("Mann-Whitney test P-value: {0:.4f}".format(p_value))
"""
Mann-Whitney test U-statistic: 69.5000
Mann-Whitney test P-value: 0.0387
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""