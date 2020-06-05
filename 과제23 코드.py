# -*- coding: utf-8 -*-


#import library
import pandas as pd
from statsmodels.formula.api import ols
from scipy import stats

#data load
df = pd.read_excel("AvgTemp.xls")

#Pearson Correlation
stats.pearsonr(df.year, df.AvgTmp)
"""
(0.6388445026294712, 2.42632074990798e-15)
"""

#Spearman Correlation
stats.spearmanr(df.year, df.AvgTmp)
"""
SpearmanrResult(correlation=0.6289457851537718, pvalue=8.673411635928697e-15)
"""

#Kendall's Tau
stats.kendalltau(df.year, df.AvgTmp)
"""
KendalltauResult(correlation=0.4591828926737606, pvalue=1.6291212306228057e-13)
"""

#Regression
lm = ols('df.AvgTmp ~ df.year', data=df).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              df.AvgTmp   R-squared:                       0.408
Model:                            OLS   Adj. R-squared:                  0.403
Method:                 Least Squares   F-statistic:                     82.74
Date:                Fri, 05 Jun 2020   Prob (F-statistic):           2.43e-15
Time:                        23:14:37   Log-Likelihood:                -109.46
No. Observations:                 122   AIC:                             222.9
Df Residuals:                     120   BIC:                             228.5
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    -33.1840      2.996    -11.074      0.000     -39.117     -27.251
df.year        0.0140      0.002      9.096      0.000       0.011       0.017
==============================================================================
Omnibus:                        1.828   Durbin-Watson:                   1.876
Prob(Omnibus):                  0.401   Jarque-Bera (JB):                1.510
Skew:                          -0.109   Prob(JB):                        0.470
Kurtosis:                       2.500   Cond. No.                     1.08e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.08e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""