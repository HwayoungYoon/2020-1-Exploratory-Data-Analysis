# -*- coding: utf-8 -*-


#library import
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#데이터 가져오기
titanic = sns.load_dataset("titanic")
titanic.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 63.0+ KB
"""

#결측값 확인
sns.heatmap(titanic.isnull())
plt.title("Distributions of null values")
plt.show()

#age의 결측값을 평균으로 대체
mean = titanic["age"].mean()
titanic["age"].fillna(mean, inplace=True)
titanic["age"].mean()

"""
Out[4]: 29.699117647058763
"""

#결측값 대체 결과 확인
sns.heatmap(titanic.isnull())
plt.title("Distributions of null values")
plt.show()

#ANOVA(일원분산분석)
model = ols('age ~ C(pclass)', titanic).fit()
print(anova_lm(model))

"""
              df         sum_sq      mean_sq          F        PR(>F)
C(pclass)    2.0   17004.449170  8502.224585  56.574385  7.481182e-24
Residual   888.0  133452.186774   150.283994        NaN           NaN
"""

#사후검정
posthoc = pairwise_tukeyhsd(titanic["age"], titanic["pclass"], alpha=0.05)
print(posthoc)

"""
 Multiple Comparison of Means - Tukey HSD, FWER=0.05 
=====================================================
group1 group2 meandiff p-adj   lower    upper  reject
-----------------------------------------------------
     1      2  -7.1812  0.001 -10.0685 -4.2939   True
     1      3 -10.6449  0.001 -12.9947  -8.295   True
     2      3  -3.4637 0.0032  -5.9514  -0.976   True
-----------------------------------------------------
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
