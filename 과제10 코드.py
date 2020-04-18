# -*- coding: utf-8 -*-

#1번
import pandas as pd

wine1 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")
wine2 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=";")

print(wine1)
print(wine2)

"""
      fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
0               7.4             0.700         0.00  ...       0.56      9.4        5
1               7.8             0.880         0.00  ...       0.68      9.8        5
2               7.8             0.760         0.04  ...       0.65      9.8        5
3              11.2             0.280         0.56  ...       0.58      9.8        6
4               7.4             0.700         0.00  ...       0.56      9.4        5
            ...               ...          ...  ...        ...      ...      ...
1594            6.2             0.600         0.08  ...       0.58     10.5        5
1595            5.9             0.550         0.10  ...       0.76     11.2        6
1596            6.3             0.510         0.13  ...       0.75     11.0        6
1597            5.9             0.645         0.12  ...       0.71     10.2        5
1598            6.0             0.310         0.47  ...       0.66     11.0        6

[1599 rows x 12 columns]
      fixed acidity  volatile acidity  citric acid  ...  sulphates  alcohol  quality
0               7.0              0.27         0.36  ...       0.45      8.8        6
1               6.3              0.30         0.34  ...       0.49      9.5        6
2               8.1              0.28         0.40  ...       0.44     10.1        6
3               7.2              0.23         0.32  ...       0.40      9.9        6
4               7.2              0.23         0.32  ...       0.40      9.9        6
            ...               ...          ...  ...        ...      ...      ...
4893            6.2              0.21         0.29  ...       0.50     11.2        6
4894            6.6              0.32         0.36  ...       0.46      9.6        5
4895            6.5              0.24         0.19  ...       0.46      9.4        6
4896            5.5              0.29         0.30  ...       0.38     12.8        7
4897            6.0              0.21         0.38  ...       0.32     11.8        6

[4898 rows x 12 columns]
"""

print("Wine1 column수 : ", len(wine1.columns), "관측지수 : ", len(wine1))
print("Wine2 column수 : ", len(wine2.columns), "관측지수 : ", len(wine2))

"""
Wine1 column수 :  12 관측지수 :  1599
Wine2 column수 :  12 관측지수 :  4898
"""

wine_concat = pd.concat([wine1, wine2])

len(wine_concat)
len(wine_concat.columns)

"""
6497
12
"""


#2번
import seaborn as sns
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

titanic = sns.load_dataset("titanic")

mean = round(titanic["age"].mean())
titanic["age"].fillna(mean, inplace=True)

Q1 = titanic["age"].quantile(0.25)
Q3 = titanic["age"].quantile(0.75)

titanic['age_cut'] = pd.cut(titanic['age'],
                            bins=[0,Q1,Q3,99],
                            labels=['Q1 미만','Q1~Q3','Q3 초과'])

model = ols('survived ~ age_cut', titanic).fit()
anova_lm(model)

""" 
             df      sum_sq   mean_sq         F    PR(>F)
age_cut     2.0    0.561989  0.280995  1.187272  0.305536
Residual  888.0  210.165283  0.236673       NaN       NaN
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))

"""
Mac address: 150075731951663
"""