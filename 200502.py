# -*- coding: utf-8 -*-

"""
와인 데이터셋 분석
"""

#import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#데이터 불러오기
wine1 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")
wine2 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=";")

#type 지정
wine1["type"] = "red"
wine2["type"] = "white"

#wine1과 wine2 합치기
wine = pd.concat([wine1, wine2])
print(wine.head)
"""
<bound method NDFrame.head of       fixed acidity  volatile acidity  citric acid  ...  alcohol  quality   type
0               7.4              0.70         0.00  ...      9.4        5    red
1               7.8              0.88         0.00  ...      9.8        5    red
2               7.8              0.76         0.04  ...      9.8        5    red
3              11.2              0.28         0.56  ...      9.8        6    red
4               7.4              0.70         0.00  ...      9.4        5    red
            ...               ...          ...  ...      ...      ...    ...
4893            6.2              0.21         0.29  ...     11.2        6  white
4894            6.6              0.32         0.36  ...      9.6        5  white
4895            6.5              0.24         0.19  ...      9.4        6  white
4896            5.5              0.29         0.30  ...     12.8        7  white
4897            6.0              0.21         0.38  ...     11.8        6  white

[6497 rows x 13 columns]>
"""

#변수별 요약통계 표시
print(wine.describe())
"""
       fixed acidity  volatile acidity  ...      alcohol      quality
count    6497.000000       6497.000000  ...  6497.000000  6497.000000
mean        7.215307          0.339666  ...    10.491801     5.818378
std         1.296434          0.164636  ...     1.192712     0.873255
min         3.800000          0.080000  ...     8.000000     3.000000
25%         6.400000          0.230000  ...     9.500000     5.000000
50%         7.000000          0.290000  ...    10.300000     6.000000
75%         7.700000          0.400000  ...    11.300000     6.000000
max        15.900000          1.580000  ...    14.900000     9.000000

[8 rows x 12 columns]
"""

#유일값 찾기
print(sorted(wine.quality.unique()))
"""
[3, 4, 5, 6, 7, 8, 9]
"""

#빈도 계산
print(wine.quality.value_counts())
"""
6    2836
5    2138
7    1079
4     216
8     193
3      30
9       5
Name: quality, dtype: int64
"""
print(pd.crosstab(index=wine.quality, columns="count"))
"""
col_0    count
quality       
3           30
4          216
5         2138
6         2836
7         1079
8          193
9            5
"""

#와인 종류에 따른 기술통계 출력
print(wine.groupby('type')[['quality']].describe().unstack('type'))
"""
                type 
quality  count  red      1599.000000
                white    4898.000000
         mean   red         5.636023
                white       5.877909
         std    red         0.807569
                white       0.885639
         min    red         3.000000
                white       3.000000
         25%    red         5.000000
                white       5.000000
         50%    red         6.000000
                white       6.000000
         75%    red         6.000000
                white       6.000000
         max    red         8.000000
                white       9.000000
dtype: float64
"""

#특정 사분위수 계산
print(wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))
"""
     quality      
type     red white
0.25     5.0   5.0
0.75     6.0   6.0
"""

#grouped 연산
grouped = wine['quality'].groupby(wine['type'])
grouped.describe().unstack('type')
"""
       type 
count  red      1599.000000
       white    4898.000000
mean   red         5.636023
       white       5.877909
std    red         0.807569
       white       0.885639
min    red         3.000000
       white       3.000000
25%    red         5.000000
       white       5.000000
50%    red         6.000000
       white       6.000000
75%    red         6.000000
       white       6.000000
max    red         8.000000
       white       9.000000
dtype: float64
"""
grouped.quantile([0.25,0.75]).unstack('type')
"""
type  red  white
0.25  5.0    5.0
0.75  6.0    6.0
"""
wine.groupby(['type'])[['quality']].agg(['std','mean'])
"""
        quality          
            std      mean
type                     
red    0.807569  5.636023
white  0.885639  5.877909
"""

#와인 종류별 품질 확인
red_wine = wine.loc[wine['type']=='red']
white_wine = wine.loc[wine['type']=='white']

sns.set_style('dark')
sns.distplot(red_wine['quality'], norm_hist=True, kde=False, color="red", label="Red Wine")
sns.distplot(white_wine['quality'], norm_hist=True, kde=False, color="white", label="White Wine")
sns.utils.axlabel("Quality Score", "Density")
plt.legend()
plt.savefig('bar_plot_16th.png', dpi=400, bbox_inches='tight')

#와인 종류별 품질 T검정
model = stats.ttest_ind(red_wine['quality'], white_wine['quality'], equal_var=False)
print(model)
"""
Ttest_indResult(statistic=-10.149363059143164, pvalue=8.168348870049682e-24)
"""

#표본 추출
df1 = wine[wine['type']=='red'].sample(n=200, replace=True)
df2 = wine[wine['type']=='white'].sample(n=200, replace=True)
wine_sample = pd.concat([df1,df2], sort=False)

#쌍대 비교 플롯
sns.pairplot(wine_sample, kind="reg", hue="type", diag_kind="hist", 
             palette=dict(red="red", white="white"), 
             vars=['quality','alcohol','residual sugar'])
"""
TypeError: Cannot cast array data from dtype('int64') to dtype('int32') according to the rule 'safe'

quality : int64
alcohol : float64
residual sugar : float64

###오류 해결 시도1(실패)
import numpy as np
wine_sample['quality'] = wine_sample['quality'].astype(np.int32)
wine_sample['alcohol'] = wine_sample['alcohol'].astype(np.int32)
wine_sample['residual sugar'] = wine_sample['residual sugar'].astype(np.int32)

###오류 해결 시도2(실패)
wine_sample['quality'] = wine_sample['quality'].astype(np.float64)
"""

plt.suptitle("Histograms and Scatter plots of Quality, Alcohol, and Residual Sugar")
plt.savefig('hist_scatter_16th.png', dpi=400, bbox_inches='tight')
