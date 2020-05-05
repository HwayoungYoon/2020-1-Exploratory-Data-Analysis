# -*- coding: utf-8 -*-

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from scipy import stats


#와인품질 데이터 불러오기
wine1 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")
wine2 = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=";")

wine1["type"] = "red"
wine2["type"] = "white"

wine = pd.concat([wine1, wine2])


#독립변수의 표준화
dependent_variable = wine['quality']

independent_variables = wine.drop(['quality','type'], axis=1)
independent_variables_standardized = (independent_variables - independent_variables.mean())/independent_variables.std()

wine_standardized = pd.concat([dependent_variable, independent_variables_standardized], axis=1)

my_formula = 'quality ~ alcohol + chlorides + pH + sulphates'

lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.214
Model:                            OLS   Adj. R-squared:                  0.214
Method:                 Least Squares   F-statistic:                     442.7
Date:                Tue, 05 May 2020   Prob (F-statistic):               0.00
Time:                        16:59:16   Log-Likelihood:                -7554.3
No. Observations:                6497   AIC:                         1.512e+04
Df Residuals:                    6492   BIC:                         1.515e+04
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      5.8184      0.010    605.698      0.000       5.800       5.837
alcohol        0.3635      0.010     36.080      0.000       0.344       0.383
chlorides     -0.1147      0.011    -10.536      0.000      -0.136      -0.093
pH            -0.0387      0.010     -3.926      0.000      -0.058      -0.019
sulphates      0.0875      0.011      8.185      0.000       0.067       0.109
==============================================================================
Omnibus:                      123.331   Durbin-Watson:                   1.647
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              257.092
Skew:                           0.030   Prob(JB):                     1.49e-56
Kurtosis:                       3.973   Cond. No.                         1.69
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""