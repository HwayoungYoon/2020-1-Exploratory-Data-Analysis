# -*- coding: utf-8 -*-

import numpy as np
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


#와인품질 데이터 회귀분석
my_formula = 'quality ~ alcohol + chlorides + density + pH + sulphates'
lm = ols(my_formula, data=wine).fit()

print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                quality   R-squared:                       0.214
Model:                            OLS   Adj. R-squared:                  0.214
Method:                 Least Squares   F-statistic:                     354.1
Date:                Mon, 04 May 2020   Prob (F-statistic):               0.00
Time:                        20:37:12   Log-Likelihood:                -7554.3
No. Observations:                6497   AIC:                         1.512e+04
Df Residuals:                    6491   BIC:                         1.516e+04
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      1.8707      4.808      0.389      0.697      -7.555      11.296
alcohol        0.3071      0.012     26.446      0.000       0.284       0.330
chlorides     -3.2883      0.314    -10.471      0.000      -3.904      -2.673
density        1.3873      4.772      0.291      0.771      -7.968      10.742
pH            -0.2421      0.062     -3.936      0.000      -0.363      -0.122
sulphates      0.5826      0.075      7.815      0.000       0.436       0.729
==============================================================================
Omnibus:                      123.279   Durbin-Watson:                   1.647
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              256.984
Skew:                           0.030   Prob(JB):                     1.57e-56
Kurtosis:                       3.972   Cond. No.                     7.85e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 7.85e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

print("\Quantities you can extract from the result:\n%s" % dir(lm))
"""
\Quantities you can extract from the result:
['HC0_se', 'HC1_se', 'HC2_se', 'HC3_se', '_HCCM', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cache', '_data_attr', '_get_robustcov_results', '_is_nested', '_use_t', '_wexog_singular_values', 'aic', 'bic', 'bse', 'centered_tss', 'compare_f_test', 'compare_lm_test', 'compare_lr_test', 'condition_number', 'conf_int', 'conf_int_el', 'cov_HC0', 'cov_HC1', 'cov_HC2', 'cov_HC3', 'cov_kwds', 'cov_params', 'cov_type', 'df_model', 'df_resid', 'diagn', 'eigenvals', 'el_test', 'ess', 'f_pvalue', 'f_test', 'fittedvalues', 'fvalue', 'get_influence', 'get_prediction', 'get_robustcov_results', 'initialize', 'k_constant', 'llf', 'load', 'model', 'mse_model', 'mse_resid', 'mse_total', 'nobs', 'normalized_cov_params', 'outlier_test', 'params', 'predict', 'pvalues', 'remove_data', 'resid', 'resid_pearson', 'rsquared', 'rsquared_adj', 'save', 'scale', 'ssr', 'summary', 'summary2', 't_test', 't_test_pairwise', 'tvalues', 'uncentered_tss', 'use_t', 'wald_test', 'wald_test_terms', 'wresid']
"""

print("\nCoefficients:\n%s" % lm.params)
"""
Coefficients:
Intercept    1.870706
alcohol      0.307070
chlorides   -3.288253
density      1.387264
pH          -0.242099
sulphates    0.582560
dtype: float64
"""

print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
"""
Adj. R-squared:
0.21
"""

print("\nF-statistsic: %.1f P-value:%.2f" % (lm.fvalue, lm.f_pvalue))
"""
F-statistsic: 354.1 P-value:0.00
"""

print("\nNumber of obs: %d Number of fitted values: %s" % (lm.nobs,len(lm.fittedvalues)))
"""
Number of obs: 6497 Number of fitted values: 6497
"""


#와인품질 데이터 선형 회귀분석 - 예측하기
new_wine = wine.iloc[0:9,]
y_predicted = lm.predict(new_wine)
y_predicted_rounded = [round(score,2) for score in y_predicted]
df2 = pd.DataFrame(y_predicted_rounded, columns = ["Predicted"])
new = pd.concat([new_wine, df2], axis=1)
new
"""
   fixed acidity  volatile acidity  citric acid  ...  quality  type  Predicted
0            7.4              0.70         0.00  ...        5   red       5.37
1            7.8              0.88         0.00  ...        5   red       5.56
2            7.8              0.76         0.04  ...        5   red       5.55
3           11.2              0.28         0.56  ...        6   red       5.59
4            7.4              0.70         0.00  ...        5   red       5.37
5            7.4              0.66         0.00  ...        5   red       5.37
6            7.9              0.60         0.06  ...        5   red       5.38
7            7.3              0.65         0.00  ...        7   red       5.56
8            7.8              0.58         0.02  ...        7   red       5.45

[9 rows x 14 columns]
"""


#보스톤 주택 가격 데이터 가져오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from sklearn.datasets import load_boston

boston = load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['PRICE'] = boston.target


#보스톤 주택가격 데이터 - 플롯
plt.figure(figsize = (15,15))
sns.heatmap(df.corr(), annot=True, fmt='.1f', cmap='Blues')
plt.suptitle("Correlation Matrix")
plt.savefig('heatmap_17th.png', dpi=400, bbox_inches='tight')

sns.pairplot(df[["PRICE", "RM", "AGE", "CHAS"]], hue="CHAS")
plt.savefig('pairplot_17th_1.png', dpi=400, bbox_inches='tight')


#로그변환
plt.scatter(df.CRIM, df.PRICE)
df["LCRIM"] = np.log(df.CRIM)
plt.scatter(df.LCRIM, df.PRICE)
plt.savefig('scatter_17th.png', dpi=400, bbox_inches='tight')

sns.pairplot(df[["PRICE", "RM", "AGE"]])
plt.savefig('pairplot_17th_2.png', dpi=400, bbox_inches='tight')


#보스톤 주택가격 데이터 - 회귀분석
lm = ols('PRICE ~ LCRIM + ZN + CHAS + NOX + RM + DIS + RAD + AGE + TAX + PTRATIO + B + LSTAT', data = df).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  PRICE   R-squared:                       0.736
Model:                            OLS   Adj. R-squared:                  0.730
Method:                 Least Squares   F-statistic:                     114.5
Date:                Mon, 04 May 2020   Prob (F-statistic):          4.64e-134
Time:                        21:13:42   Log-Likelihood:                -1503.3
No. Observations:                 506   AIC:                             3033.
Df Residuals:                     493   BIC:                             3088.
Df Model:                          12                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     36.6597      5.213      7.032      0.000      26.417      46.902
LCRIM          0.4093      0.277      1.477      0.140      -0.135       0.954
ZN             0.0466      0.014      3.310      0.001       0.019       0.074
CHAS           2.8652      0.862      3.322      0.001       1.171       4.560
NOX          -18.1912      3.866     -4.705      0.000     -25.787     -10.595
RM             3.8373      0.419      9.150      0.000       3.013       4.661
DIS           -1.4041      0.195     -7.183      0.000      -1.788      -1.020
RAD            0.1821      0.073      2.509      0.012       0.040       0.325
AGE           -0.0019      0.013     -0.142      0.887      -0.028       0.024
TAX           -0.0115      0.003     -3.390      0.001      -0.018      -0.005
PTRATIO       -0.9173      0.131     -6.987      0.000      -1.175      -0.659
B              0.0109      0.003      4.011      0.000       0.006       0.016
LSTAT         -0.5597      0.051    -10.986      0.000      -0.660      -0.460
==============================================================================
Omnibus:                      168.712   Durbin-Watson:                   1.079
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              754.512
Skew:                           1.425   Prob(JB):                    1.44e-164
Kurtosis:                       8.260   Cond. No.                     1.54e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.54e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""