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

#the "C" indicates categorical data
model = ols('survived ~ C(pclass)', titanic).fit()
print(anova_lm(model))
