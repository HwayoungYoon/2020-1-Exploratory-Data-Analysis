# -*- coding: utf-8 -*-

#import library
import numpy as np
from scipy import stats

#data 입력
score1 = np.array([70,60,45,90,95,80,85])
score2 = np.array([100,95,55,65,75,75])

#Mann-Whitney Test
u, p_value = stats.mannwhitneyu(score1, score2)

print("Mann-Whitney test U : ", u)
print("Mann-Whitney test P-Value : ", p_value)
"""
Mann-Whitney test U :  19.5
Mann-Whitney test P-Value :  0.4430458847542784
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 141991317885390
"""