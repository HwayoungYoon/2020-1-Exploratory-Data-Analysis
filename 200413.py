# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:59:47 2020

@author: ghkdu
"""

#titanic 데이터에서 티켓클래스가 생존에 미치는 영향
#ANOVA
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

iris = sns.load_dataset("titanic")
print(titanic)

"""
     survived  pclass     sex        age  ...  deck  embark_town  alive  alone
0           0       3    male  22.000000  ...   NaN  Southampton     no  False
1           1       1  female  38.000000  ...     C    Cherbourg    yes  False
2           1       3  female  26.000000  ...   NaN  Southampton    yes   True
3           1       1  female  35.000000  ...     C  Southampton    yes  False
4           0       3    male  35.000000  ...   NaN  Southampton     no   True
..        ...     ...     ...        ...  ...   ...          ...    ...    ...
886         0       2    male  27.000000  ...   NaN  Southampton     no   True
887         1       1  female  19.000000  ...     B  Southampton    yes   True
888         0       3  female  29.699118  ...   NaN  Southampton     no  False
889         1       1    male  26.000000  ...     C    Cherbourg    yes   True
890         0       3    male  32.000000  ...   NaN   Queenstown     no   True

[891 rows x 15 columns]
"""


#the "C" indicates categorical data
model = ols('survived ~ C(pclass)', titanic).fit()
print(anova_lm(model))

"""
              df      sum_sq    mean_sq          F        PR(>F)
C(pclass)    2.0   24.333912  12.166956  57.964818  2.183247e-24
Residual   888.0  186.393360   0.209902        NaN           NaN
"""
