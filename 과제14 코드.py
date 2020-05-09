# -*- coding: utf-8 -*-

#import library
import pandas as pd
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial

#데이터 가져오기
crabs = pd.read_csv("horseshoe.csv")

#로지스틱 회귀
model = glm("satellite_1 ~ width + spine", data=crabs, family=Binomial()).fit()
print(model.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      170
Model Family:                Binomial   Df Model:                            2
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -97.218
Date:                Wed, 06 May 2020   Deviance:                       194.44
Time:                        17:13:38   Pearson chi2:                     165.
No. Iterations:                     4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    -12.4410      2.723     -4.568      0.000     -17.779      -7.103
width          0.4980      0.102      4.887      0.000       0.298       0.698
spine          0.0282      0.220      0.128      0.898      -0.402       0.458
==============================================================================
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 170357387571136
"""