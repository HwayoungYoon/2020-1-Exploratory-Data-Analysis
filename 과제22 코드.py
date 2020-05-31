# -*- coding: utf-8 -*-


#import library
import numpy as np
from scipy.stats import fisher_exact


#import data
data = np.array([[19,1],[6,14]])


#fisher 정확 검정
oddsratio, pvalue = fisher_exact(data)
print("P-value:", pvalue)
"""
P-value: 3.9313721182464246e-05
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""