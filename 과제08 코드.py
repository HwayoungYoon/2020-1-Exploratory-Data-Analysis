# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:29:29 2020

@author: ghkdu
"""

import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

iris = sns.load_dataset("iris")
print(iris)

model = ols('sepal_length ~ C(species)', iris).fit()
print(anova_lm(model))


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
