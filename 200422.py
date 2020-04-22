# -*- coding: utf-8 -*-

import seaborn as sns
titanic = sns.load_dataset("titanic")


#행선택
##인덱스 활용
titanic.iloc[2]
"""
survived                 1
pclass                   3
sex                 female
age                     26
sibsp                    0
parch                    0
fare                 7.925
embarked                 S
class                Third
who                  woman
adult_male           False
deck                   NaN
embark_town    Southampton
alive                  yes
alone                 True
Name: 2, dtype: object
"""

##행번호 활용
titanic.loc[[0,1,5,10,20],:]
"""
    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0          0       3    male  22.0  ...   NaN  Southampton     no  False
1          1       1  female  38.0  ...     C    Cherbourg    yes  False
5          0       3    male   NaN  ...   NaN   Queenstown     no   True
10         1       3  female   4.0  ...     G  Southampton    yes  False
20         0       2    male  35.0  ...   NaN  Southampton     no   True

[5 rows x 15 columns]
"""

##조건 활용
lower = titanic["age"].mean()
titanic[titanic['age'] < lower]
"""
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0           0       3    male  22.0  ...   NaN  Southampton     no  False
2           1       3  female  26.0  ...   NaN  Southampton    yes   True
7           0       3    male   2.0  ...   NaN  Southampton     no  False
8           1       3  female  27.0  ...   NaN  Southampton    yes  False
9           1       2  female  14.0  ...   NaN    Cherbourg    yes  False
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
883         0       2    male  28.0  ...   NaN  Southampton     no   True
884         0       3    male  25.0  ...   NaN  Southampton     no   True
886         0       2    male  27.0  ...   NaN  Southampton     no   True
887         1       1  female  19.0  ...     B  Southampton    yes   True
889         1       1    male  26.0  ...     C    Cherbourg    yes   True

[384 rows x 15 columns]
"""

##isin() 활용
titanic[titanic['embark_town'].isin(['Southampton','Queenstown'])]
"""
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0           0       3    male  22.0  ...   NaN  Southampton     no  False
2           1       3  female  26.0  ...   NaN  Southampton    yes   True
3           1       1  female  35.0  ...     C  Southampton    yes  False
4           0       3    male  35.0  ...   NaN  Southampton     no   True
5           0       3    male   NaN  ...   NaN   Queenstown     no   True
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
885         0       3  female  39.0  ...   NaN   Queenstown     no  False
886         0       2    male  27.0  ...   NaN  Southampton     no   True
887         1       1  female  19.0  ...     B  Southampton    yes   True
888         0       3  female   NaN  ...   NaN  Southampton     no  False
890         0       3    male  32.0  ...   NaN   Queenstown     no   True

[721 rows x 15 columns]
"""


#열선택
##1개 열 선택
print(titanic.deck)
print(titanic['deck'])
"""
0      NaN
1        C
2      NaN
3        C
4      NaN

886    NaN
887      B
888    NaN
889      C
890    NaN
Name: deck, Length: 891, dtype: category
Categories (7, object): [A, B, C, D, E, F, G]
"""

##2개 이상 열 선택
titanic.loc[:,['survived','pclass','age']]
titanic[['survived','pclass','age']]
"""
     survived  pclass   age
0           0       3  22.0
1           1       1  38.0
2           1       3  26.0
3           1       1  35.0
4           0       3  35.0
..        ...     ...   ...
886         0       2  27.0
887         1       1  19.0
888         0       3   NaN
889         1       1  26.0
890         0       3  32.0

[891 rows x 3 columns]
"""


#Group by
##그룹될 컬럼만 지정(대상 컬럼 1개)
import pandas as pd
grouped = titanic['age'].groupby(titanic['sex'])

grouped.count()
"""
sex
female    261
male      453
Name: age, dtype: int64
"""

grouped.mean()
"""
sex
female    27.915709
male      30.726645
Name: age, dtype: float64
"""

##수치연산을 위한 그룹 지정(대상 컬럼 여러개)
titanic.groupby('sex').mean()
"""
        survived    pclass        age  ...       fare  adult_male     alone
sex                                    ...                                 
female  0.742038  2.159236  27.915709  ...  44.479818    0.000000  0.401274
male    0.188908  2.389948  30.726645  ...  25.523893    0.930676  0.712305

[2 rows x 8 columns]
"""


#데이터 붙이기
##옆으로 붙이기
import pandas as pd

a1 = pd.DataFrame([0,1])
a2 = pd.DataFrame([2,3,4])
a3 = pd.DataFrame([5,6,7,8,9,10])

pd.concat([a1,a2,a3], axis=1)
"""
     0    0   0
0  0.0  2.0   5
1  1.0  3.0   6
2  NaN  4.0   7
3  NaN  NaN   8
4  NaN  NaN   9
5  NaN  NaN  10
"""

##아래로 붙이기
import pandas as pd

data1 = {'종가':[5700,5800], '거래량':[555850,282163]}
index1 = ['2020-04-12', '2020-04-13']
df1 = pd.DataFrame(data=data1, index=index1)

data2 = {'종가':[5750,5799], '거래량':[483689,791946]}
index2 = ['2020-04-14', '2020-04-15']
df2 = pd.DataFrame(data=data2, index=index2)

df = df1.append(df2)
print(df)
dfdf = pd.concat([df1,df2])
print(dfdf)
"""
              종가     거래량
2020-04-12  5700  555850
2020-04-13  5800  282163
2020-04-14  5750  483689
2020-04-15  5799  791946
"""

##Merge
df1 = pd.DataFrame({'동이름':[101,102,103],
                    '동대표':['오달수','이성재','배용준']})
df2 = pd.DataFrame({'세대주':['오달수','이성재','배용준'],
                    '세대원':[3,4,5]})

df_merge = pd.merge(df1, df2, left_on="동대표", right_on="세대주")
print(df_merge)
"""
   동이름  동대표  세대주  세대원
0  101  오달수  오달수    3
1  102  이성재  이성재    4
2  103  배용준  배용준    5
"""
