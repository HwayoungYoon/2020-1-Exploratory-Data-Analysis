# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:25:23 2020

@author: ghkdu
"""

#titanic 데이터 가져오기
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic.columns
titanic.describe()
print(pd.crosstab(index=titanic["survived"], columns="count"))
print(pd.crosstab(index=titanic["pclass"], columns="count"))

"""
col_0     count
survived       
0           549
1           342
col_0   count
pclass       
1         216
2         184
3         491
"""


#titanic 승객들의 연령 히스토그램
import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.hist(titanic["age"], bins=50, color='b')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Age of titanic passengers', fontsize=14, fontweight='bold')
ax1.set_title('')
plt.savefig('C:\Python\Python37-32\histogram_titanic_age.png', dpi=400, bbox_inches='tight')
plt.show()


#titanic 승객들의 연령(1표본 t검정)
from scipy import stats

mean = titanic["age"].mean()
titanic["age"].fillna(mean, inplace=True)

titanic["age"].mean()

stats.ttest_1samp(titanic["age"], 40)

"""
Ttest_1sampResult(statistic=-23.64844607732537, pvalue=2.529496530169441e-96)
"""


#titanic 승객들의 성별 연령 차이(2표본 t검정)
from scipy import stats

sample1 = titanic[titanic['sex'] == 'female']
sample2 = titanic[titanic['sex'] == 'male']

stats.ttest_ind(sample1['age'], sample2['age'], equal_var=False)

"""
Ttest_indResult(statistic=-2.5256556328842286, pvalue=0.011785333384194916)
"""


#titanic 승객들의 생존별 연령 차이(2표본 t검정)
from scipy import stats

sample1 = titanic[titanic['survived'] == 1]
sample2 = titanic[titanic['survived'] == 0]

stats.ttest_ind(sample1['age'], sample2['age'], equal_var=False)

"""
Ttest_indResult(statistic=-2.0385172031950463, pvalue=0.04189090646311582)
"""


#titanic 승객들의 생존과 티켓클래스의 상관(카이제곱 검정)
from scipy.stats import chi2_contingency

survived_class = pd.crosstab(titanic['survived'], titanic['pclass'])
print(survived_class)

"""
pclass      1   2    3
survived              
0          80  97  372
1         136  87  119
"""

chi2, p ,dof, ex = chi2_contingency(survived_class)
print("Chi-square:", chi2)
print("P-value:", p)

"""
Chi-square: 102.88898875696056
P-value: 4.549251711298793e-23
"""