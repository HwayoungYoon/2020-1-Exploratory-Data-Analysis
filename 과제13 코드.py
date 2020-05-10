# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial

crabs = pd.read_csv("horseshoe.csv")


#모든 변수에 대해 히스토그램 또는 산점도를 생성하여 형태 확인
crabs.hist(bins=30, figsize=(15,10))
sns.pairplot(data=crabs, y_vars=['satellite_1'], x_vars=['width', 'spine', 'weight'])
plt.suptitle("Pair plots of width, spine, weight by satellite_1")


#상관행렬
plt.figure(figsize=(15,10))
sns.heatmap(crabs.corr(), annot=True)


#로지스틱 회귀
model = glm('satellite_1 ~ color + spine + width + weight', data=crabs, family=Binomial()).fit()
print(model.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      168
Model Family:                Binomial   Df Model:                            4
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -93.330
Date:                Sun, 10 May 2020   Deviance:                       186.66
Time:                        19:17:56   Pearson chi2:                     170.
No. Iterations:                     5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -7.0078      3.804     -1.842      0.065     -14.463       0.447
color         -0.5915      0.242     -2.447      0.014      -1.065      -0.118
spine          0.2717      0.241      1.127      0.260      -0.201       0.744
width          0.2733      0.189      1.443      0.149      -0.098       0.644
weight         0.0008      0.001      1.149      0.250      -0.001       0.002
==============================================================================
"""

model2 = glm('satellite_1 ~ color + width + weight', data=crabs, family=Binomial()).fit()
print(model2.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      169
Model Family:                Binomial   Df Model:                            3
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -93.962
Date:                Sun, 10 May 2020   Deviance:                       187.92
Time:                        19:18:21   Pearson chi2:                     171.
No. Iterations:                     5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -6.9128      3.766     -1.836      0.066     -14.294       0.468
color         -0.4937      0.225     -2.197      0.028      -0.934      -0.053
width          0.2872      0.187      1.533      0.125      -0.080       0.654
weight         0.0007      0.001      1.085      0.278      -0.001       0.002
==============================================================================
"""

model3 = glm('satellite_1 ~ color + width', data=crabs, family=Binomial()).fit()
print(model3.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      170
Model Family:                Binomial   Df Model:                            2
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -94.561
Date:                Sun, 10 May 2020   Deviance:                       189.12
Time:                        19:19:50   Pearson chi2:                     170.
No. Iterations:                     5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -9.5618      2.883     -3.317      0.001     -15.212      -3.912
color         -0.5090      0.224     -2.276      0.023      -0.947      -0.071
width          0.4583      0.104      4.406      0.000       0.254       0.662
==============================================================================
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 170357387571136
"""