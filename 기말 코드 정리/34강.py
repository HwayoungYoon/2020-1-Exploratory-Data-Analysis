# -*- coding: utf-8 -*-
"""
34강: 산점도, 상관계수, 상관행렬 플롯
"""


"""
산점도
"""
#scatter plot: 200405.py 참고
#프로그램
import seaborn as sns
sns.set()

df = sns.load_dataset("iris")
sns.pairplot(df, hue = "species", size = 2.5)


"""
상관계수
"""
import pandas as pd
from scipy import stats

data = pd.read_csv("altman_11_1.txt", header=None)
data.columns = ['vcf', 'glucose']

y = data.vcf
x = data.glucose

corr = {}
#Pearson Correlation
corr['Pearson'], _ = stats.pearsonr(x, y)
#Spearman Correlation
corr['Spearman'], _ = stats.spearmanr(x, y)
#Kendall's Tau
corr['Kendall'], _ = stats.kendalltau(x, y)

print(corr)


"""
상관행렬 플롯
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rs = np.random.RandomState(0)
df = pd.DataFrame(rs.normal(size = (10, 10)))
df.corr()

plt.figure(figsize = (10, 8))
sns.heatmap(df.corr(), annot = True, fmt = '.2f', cmap = 'Blues')
plt.title("Correlations", position = (0.5, 1.0+0.05), fontsize = 15)
