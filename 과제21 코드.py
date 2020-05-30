# -*- coding: utf-8 -*-


#import library
import numpy as np
from scipy.stats import chi2_contingency


#import data
data = np.array([[512, 313],[89,19]])


#카이제곱검정
chi2, p, dof, ex = chi2_contingency(data)
print("Chi-square:", chi2)
print("P-value:", p)
print("Degree of freedom:", dof)
"""
Chi-square: 16.3717737289348
P-value: 5.205468345876068e-05
Degree of freedom: 1
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""