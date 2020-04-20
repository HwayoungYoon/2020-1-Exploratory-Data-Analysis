# -*- coding: utf-8 -*-

#library 선언
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


#age의 결측값을 평균으로 대체
mean = titanic["age"].mean()
titanic["age"].fillna(mean, inplace=True)


#age의 표본평균과 표본표준편차
mean_age = titanic["age"].mean()
std_age = titanic["age"].std()


#이상치가 있는 인덱스 가져오기
upper = mean_age + 3*std_age
lower = mean_age - 3*std_age
idx_nm_1 = titanic[(titanic["age"] > upper) | (titanic["age"] < lower)].index


#이상치가 있는 행의 데이터 프린트
print(titanic.iloc[idx_nm_1])

"""
     survived  pclass   sex   age  ...  deck  embark_town  alive  alone
96          0       1  male  71.0  ...     A    Cherbourg     no   True
116         0       3  male  70.5  ...   NaN   Queenstown     no   True
493         0       1  male  71.0  ...   NaN    Cherbourg     no   True
630         1       1  male  80.0  ...     A  Southampton    yes   True
672         0       2  male  70.0  ...   NaN  Southampton     no   True
745         0       1  male  70.0  ...     B  Southampton     no  False
851         0       3  male  74.0  ...   NaN  Southampton     no   True

[7 rows x 15 columns]
"""


#데이터프레임에서 이상치 삭제
titanic.drop(idx_nm_1, inplace=True)
len(titanic)

"""
884
"""


#pair plot
sns.pairplot(titanic, vars=["survived","age","pclass"], hue="survived")
plt.title("Titanic Data의 Pair Plot")
plt.savefig('pairplot_titanic.png', bbox_inches='tight')


#이원분산분석
titanic['age_cut'] = pd.cut(titanic["age"], 
                            bins=[10,20,30,40],
                            labels=['10대이하','20대','30대이상'])

model = ols('survived ~ C(pclass) * age_cut', titanic).fit()
anova_lm(model)

"""
                      df      sum_sq    mean_sq          F        PR(>F)
C(pclass)            2.0   21.840441  10.920220  54.288779  1.424306e-22
age_cut              2.0    0.337250   0.168625   0.838303  4.328980e-01
C(pclass):age_cut    4.0    0.871730   0.217932   1.083429  3.636585e-01
Residual           668.0  134.368600   0.201151        NaN           NaN
"""