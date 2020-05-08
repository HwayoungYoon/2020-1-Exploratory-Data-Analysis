# -*- coding: utf-8 -*-

#library import
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial


#데이터 가져오기
crabs = pd.read_csv("horseshoe.csv")


#색상별 satellite의 수
sns.boxplot(x="color", y="satellite", data=crabs)


#다변량 로지스틱 회귀
model = glm("satellite_1 ~ width + color", data=crabs, family=Binomial()).fit()
print(model.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      170
Model Family:                Binomial   Df Model:                            2
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -94.561
Date:                Wed, 06 May 2020   Deviance:                       189.12
Time:                        15:59:25   Pearson chi2:                     170.
No. Iterations:                     5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -9.5618      2.883     -3.317      0.001     -15.212      -3.912
width          0.4583      0.104      4.406      0.000       0.254       0.662
color         -0.5090      0.224     -2.276      0.023      -0.947      -0.071
==============================================================================
"""


#color별 satellite 로지스틱 그래프
sns.lmplot(x="width", y="satellite_1", col="color", data=crabs, height=3, logistic=True)