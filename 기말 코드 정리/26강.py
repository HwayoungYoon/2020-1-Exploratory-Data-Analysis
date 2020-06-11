# -*- coding: utf-8 -*-
"""
26강: 모집단이 정규분포인 경우 평균검정(T-test)
"""


"""
일표본검정 - 일표본 T검정
"""
import numpy as np
import scipy.stats as stats

data = np.array([5260,5470,5640,6180,6390,6515,6805,7515,7515,8320,8770])
checkValue = 7225

stats.ttest_1samp(data, checkValue)


"""
일표본검정 - Wilcoxon 부호 순위합 검정
"""
import numpy as np
import scipy.stats as stats

data = np.array([5260,5470,5640,6180,6390,6515,6805,7515,7515,8320,8770])
checkValue = 7225

rank, pVal = stats.wilcoxon(data-checkValue)

if pVal < 0.05:
    issignificant = 'unlikely'
else:
    issignificant = 'likely'

print(('It is ' + issignificant + ' that the value is {0:d}'.format(checkValue)))


"""
일표본검정 - 대응표본 T검정
"""
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(1234)
data = np.random.randn(10)+0.1
data1 = np.random.randn(10)*5
data2 = data1 + data

stats.ttest_1samp(data, 0)
stats.ttest_rel(data2, data1)

box_plot_data = [data1, data2]
box_labels = ["before", "after"]
plt.boxplot(box_plot_data, labels = box_labels)


"""
이표본 검정 - 독립표본 T검정
"""
import numpy as np
import scipy.stats as stats

group1 = np.array([5260,5470,5640,6180,6390,6515,6805,7515,7515,8230,8770])
group2 = np.array([3910,4220,3885,5160,5645,4680,5265,5975,6790,6900,7335])

t_statistic, pVal = stats.ttest_ind(group1, group2)

print("T_statistic: {0:.2f}, P-value: {1:.2f}".format(t_statistic, pVal))


"""
이표본 검정 - Mann-Whitney 검정
"""
import pandas as pd
import numpy as np
import scipy.stats as stats

energ = pd.read_csv("altman94.txt", header=None)

group1 = energ[energ.iloc[:,1] == 1][0]
group2 = energ[energ.iloc[:,1] == 0][0]

np.mean(group1)
np.mean(group2)

u, p_value = stats.mannwhitneyu(group1, group2)
print("Mann-Whiteny test U-statistic", u)
print("Mann-Whiteny test P-value", p_value)