# -*- coding: utf-8 -*-

#Box Plot
import matplotlib.pyplot as plt
import pandas as pd

loc = pd.read_csv("loc.csv")
loc

"""
    num  before  after  d
0     1      16     14 -2
1     2       7     11  4
2     3      11     14  3
3     4      11     15  4
4     5       6      4 -2
5     6       3      2 -1
6     7       8     11  3
7     8      10     12  2
8     9      12     18  6
9    10       6      8  2
10   11      10     12  2
11   12       7      8  1
12   13       5      5  0
13   14       7     11  4
14   15       9     10  1
15   16      10      9 -1
16   17       4      7  3
17   18       7      8  1
18   19      11     14  3
19   20       3      1 -2
20   21       9      9  0
21   22      11     13  2
22   23       9     13  4
23   24      12     17  5
24   25       8     11  3
25   26      10      9 -1
26   27      13     16  3
27   28      11     15  4
28   29       4      7  3
29   30      13     15  2
30   31       6      5 -1
31   32      12     19  7
32   33       2      3  1
33   34      15     14 -1
34   35      10     12  2
35   36       7     12  5
36   37      13     16  3
37   38       5      6  1
38   39       7     12  5
39   40       9     10  1
40   41       8     10  2
41   42       8     11  3
42   43       8     10  2
43   44      12     17  5
44   45      10     13  3
45   46       6      8  2
46   47      14     15  1
47   48       5      6  1
48   49       9     10  1
49   50      11     13  2
"""

data_to_plot = [loc["before"], loc["after"]]

fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(1,1,1)

ax.boxplot(data_to_plot)

ax.set_xticklabels(['before','after'])
fig.savefig('boxplot_loc.png', bbox_inches='tight')


#대응표본 T검정
from scipy import stats
stats.ttest_rel(loc['before'], loc['after'])

"""
Ttest_relResult(statistic=-6.787730006651186, pvalue=1.4146824080089325e-08)
"""


#종에 따른 꽃받침의 길이의 차이
##ANOVA
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

iris = sns.load_dataset("iris")

model = ols('sepal_length ~ species', iris).fit()
print(anova_lm(model))

"""
             df     sum_sq    mean_sq           F        PR(>F)
species     2.0  63.212133  31.606067  119.264502  1.669669e-31
Residual  147.0  38.956200   0.265008         NaN           NaN
"""

##Box Plot
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = sns.load_dataset("iris")

sns.boxplot(x="species", y="sepal_length", data=iris)
plt.savefig('boxplot_iris_spe_sl_1.png', bbox_inches='tight')

##이상치 삭제
###virginica VS no-virginica
sample1 = iris[iris['species'] == 'virginica']
sample2 = iris[iris['species'] != 'virginica']

###IQR calculation for virginica
Q1 = sample1["sepal_length"].quantile(0.25)
Q3 = sample1["sepal_length"].quantile(0.75)
IQR = Q3 - Q1

###check rows for outliers
idx_nm_1 = sample1[sample1['sepal_length'] < Q1-IQR*1.5].index
sample11 = sample1.drop(idx_nm_1)

###concatenation sample2, sample11
filtered_iris = pd.concat([sample2, sample11], axis=0)
sns.boxplot(x="species", y="sepal_length", data=filtered_iris)
plt.savefig('boxplot_iris_spe_sl_2.png', bbox_inches='tight')


##사후검정(Post Hoc Analysis)
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd

iris = sns.load_dataset("iris")

posthoc = pairwise_tukeyhsd(iris['sepal_length'], iris['species'], alpha=0.05)
print(posthoc)

"""
   Multiple Comparison of Means - Tukey HSD, FWER=0.05   
=========================================================
  group1     group2   meandiff p-adj lower  upper  reject
---------------------------------------------------------
    setosa versicolor     0.93 0.001 0.6862 1.1738   True
    setosa  virginica    1.582 0.001 1.3382 1.8258   True
versicolor  virginica    0.652 0.001 0.4082 0.8958   True
---------------------------------------------------------
"""