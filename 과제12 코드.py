# -*- coding: utf-8 -*-


#import library
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor
from patsy import dmatrices


#데이터 가져오기
boston = load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['PRICE'] = boston.target


#데이터 형태 확인
df.info()
df.std()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   CRIM     506 non-null    float64
 1   ZN       506 non-null    float64
 2   INDUS    506 non-null    float64
 3   CHAS     506 non-null    float64
 4   NOX      506 non-null    float64
 5   RM       506 non-null    float64
 6   AGE      506 non-null    float64
 7   DIS      506 non-null    float64
 8   RAD      506 non-null    float64
 9   TAX      506 non-null    float64
 10  PTRATIO  506 non-null    float64
 11  B        506 non-null    float64
 12  LSTAT    506 non-null    float64
 13  PRICE    506 non-null    float64
dtypes: float64(14)
memory usage: 55.4 KB
Out[3]: 
CRIM         8.601545
ZN          23.322453
INDUS        6.860353
CHAS         0.253994
NOX          0.115878
RM           0.702617
AGE         28.148861
DIS          2.105710
RAD          8.707259
TAX        168.537116
PTRATIO      2.164946
B           91.294864
LSTAT        7.141062
PRICE        9.197104
dtype: float64
"""


#histogram
df.hist(bins=30, figsize=(15,10))
"""
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x0A89A5D0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0AF96E90>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0AFB8F70>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0AFE3610>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0B0046F0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B0247D0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B046930>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B0663F0>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0B066990>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B086B30>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B0C7C30>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B0E8D10>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0B10ADF0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B126ED0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B149FB0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0B168AF0>]],
      dtype=object)
"""


#pair plot
sns.pairplot(data=df, y_vars=['PRICE'], x_vars=['PTRATIO','TAX','RAD','B'])
plt.suptitle("Pair plots of PTRATIO, TAX, PRICE by PRICE")
"""
Text(0.5, 0.98, 'Pair plots of PTRATIO, TAX, PRICE by PRICE')
"""


#log 변환
df['LB'] = np.log(df.B)
sns.pairplot(data=df, y_vars=['PRICE'], x_vars=['B','LB'])
"""
<seaborn.axisgrid.PairGrid at 0xa89a510>
"""

df['LCRIM'] = np.log(df.CRIM)
sns.pairplot(data=df, y_vars=['PRICE'], x_vars=['CRIM','LCRIM'])
"""
<seaborn.axisgrid.PairGrid at 0xb516270>
"""


#상관행렬
plt.figure(figsize=(18,18))
sns.heatmap(data=df.corr(), annot=True, fmt='.2f', linewidths=.5, cmap='Blues')
"""
<matplotlib.axes._subplots.AxesSubplot at 0xef2dd0>
"""


#회귀분석
lm = ols('PRICE ~ LCRIM + CRIM + ZN + INDUS + CHAS + NOX + RM + DIS + RAD + TAX + PTRATIO + LB + B + LSTAT + AGE', data=df).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  PRICE   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.738
Method:                 Least Squares   F-statistic:                     95.66
Date:                Fri, 01 May 2020   Prob (F-statistic):          7.76e-135
Time:                        20:42:05   Log-Likelihood:                -1494.1
No. Observations:                 506   AIC:                             3020.
Df Residuals:                     490   BIC:                             3088.
Df Model:                          15                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     37.5877      5.580      6.736      0.000      26.623      48.552
LCRIM          0.8117      0.296      2.741      0.006       0.230       1.394
CRIM          -0.1415      0.035     -4.024      0.000      -0.211      -0.072
ZN             0.0568      0.014      4.011      0.000       0.029       0.085
INDUS          0.0007      0.061      0.011      0.991      -0.120       0.121
CHAS           2.6510      0.855      3.099      0.002       0.970       4.332
NOX          -21.2225      3.969     -5.347      0.000     -29.021     -13.424
RM             3.8167      0.415      9.196      0.000       3.001       4.632
DIS           -1.4856      0.198     -7.502      0.000      -1.875      -1.096
RAD            0.2091      0.075      2.778      0.006       0.061       0.357
TAX           -0.0123      0.004     -3.281      0.001      -0.020      -0.005
PTRATIO       -0.9070      0.131     -6.937      0.000      -1.164      -0.650
LB             0.6489      0.642      1.011      0.313      -0.613       1.911
B              0.0051      0.006      0.886      0.376      -0.006       0.016
LSTAT         -0.5401      0.051    -10.674      0.000      -0.640      -0.441
AGE           -0.0040      0.013     -0.305      0.761      -0.030       0.022
==============================================================================
Omnibus:                      174.076   Durbin-Watson:                   1.102
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              752.585
Skew:                           1.489   Prob(JB):                    3.79e-164
Kurtosis:                       8.179   Cond. No.                     1.64e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.64e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

lm = ols('PRICE ~ LCRIM + CRIM + ZN + CHAS + NOX + RM + DIS + RAD + TAX + PTRATIO + LB + B + LSTAT + AGE', data=df).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  PRICE   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.738
Method:                 Least Squares   F-statistic:                     102.7
Date:                Fri, 01 May 2020   Prob (F-statistic):          7.51e-136
Time:                        20:43:01   Log-Likelihood:                -1494.1
No. Observations:                 506   AIC:                             3018.
Df Residuals:                     491   BIC:                             3082.
Df Model:                          14                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     37.5857      5.572      6.745      0.000      26.638      48.534
LCRIM          0.8121      0.294      2.761      0.006       0.234       1.390
CRIM          -0.1416      0.035     -4.040      0.000      -0.210      -0.073
ZN             0.0567      0.014      4.025      0.000       0.029       0.084
CHAS           2.6520      0.850      3.119      0.002       0.982       4.322
NOX          -21.2127      3.870     -5.482      0.000     -28.816     -13.609
RM             3.8163      0.413      9.243      0.000       3.005       4.627
DIS           -1.4860      0.193     -7.686      0.000      -1.866      -1.106
RAD            0.2088      0.072      2.906      0.004       0.068       0.350
TAX           -0.0122      0.003     -3.646      0.000      -0.019      -0.006
PTRATIO       -0.9068      0.129     -7.012      0.000      -1.161      -0.653
LB             0.6490      0.641      1.012      0.312      -0.611       1.909
B              0.0050      0.006      0.887      0.376      -0.006       0.016
LSTAT         -0.5401      0.050    -10.707      0.000      -0.639      -0.441
AGE           -0.0040      0.013     -0.305      0.760      -0.030       0.022
==============================================================================
Omnibus:                      174.076   Durbin-Watson:                   1.102
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              752.579
Skew:                           1.489   Prob(JB):                    3.80e-164
Kurtosis:                       8.179   Cond. No.                     1.63e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.63e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

lm = ols('PRICE ~ LCRIM + CRIM + ZN + CHAS + NOX + RM + DIS + RAD + TAX + PTRATIO + LB + B + LSTAT', data=df).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  PRICE   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.739
Method:                 Least Squares   F-statistic:                     110.8
Date:                Fri, 01 May 2020   Prob (F-statistic):          7.32e-137
Time:                        20:43:24   Log-Likelihood:                -1494.1
No. Observations:                 506   AIC:                             3016.
Df Residuals:                     492   BIC:                             3075.
Df Model:                          13                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     37.6557      5.562      6.770      0.000      26.727      48.584
LCRIM          0.8001      0.291      2.748      0.006       0.228       1.372
CRIM          -0.1411      0.035     -4.034      0.000      -0.210      -0.072
ZN             0.0571      0.014      4.065      0.000       0.029       0.085
CHAS           2.6397      0.848      3.111      0.002       0.973       4.307
NOX          -21.4666      3.776     -5.685      0.000     -28.885     -14.048
RM             3.7903      0.404      9.390      0.000       2.997       4.583
DIS           -1.4687      0.185     -7.956      0.000      -1.831      -1.106
RAD            0.2117      0.071      2.975      0.003       0.072       0.352
TAX           -0.0123      0.003     -3.660      0.000      -0.019      -0.006
PTRATIO       -0.9103      0.129     -7.074      0.000      -1.163      -0.657
LB             0.6532      0.641      1.020      0.308      -0.606       1.912
B              0.0050      0.006      0.872      0.384      -0.006       0.016
LSTAT         -0.5451      0.048    -11.437      0.000      -0.639      -0.451
==============================================================================
Omnibus:                      172.320   Durbin-Watson:                   1.105
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              734.364
Skew:                           1.478   Prob(JB):                    3.43e-160
Kurtosis:                       8.108   Cond. No.                     1.61e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.61e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

lm = ols('PRICE ~ LCRIM + CRIM + ZN + CHAS + NOX + RM + DIS + RAD + TAX + PTRATIO + LB + LSTAT', data=df).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  PRICE   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.739
Method:                 Least Squares   F-statistic:                     120.0
Date:                Fri, 01 May 2020   Prob (F-statistic):          9.53e-138
Time:                        20:43:46   Log-Likelihood:                -1494.5
No. Observations:                 506   AIC:                             3015.
Df Residuals:                     493   BIC:                             3070.
Df Model:                          12                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     36.6185      5.432      6.741      0.000      25.945      47.292
LCRIM          0.7637      0.288      2.651      0.008       0.198       1.330
CRIM          -0.1398      0.035     -4.001      0.000      -0.208      -0.071
ZN             0.0566      0.014      4.033      0.000       0.029       0.084
CHAS           2.6564      0.848      3.133      0.002       0.990       4.322
NOX          -21.5815      3.773     -5.721      0.000     -28.994     -14.169
RM             3.7862      0.404      9.382      0.000       2.993       4.579
DIS           -1.4732      0.184     -7.986      0.000      -1.836      -1.111
RAD            0.2158      0.071      3.040      0.002       0.076       0.355
TAX           -0.0124      0.003     -3.703      0.000      -0.019      -0.006
PTRATIO       -0.9044      0.128     -7.039      0.000      -1.157      -0.652
LB             1.1464      0.301      3.811      0.000       0.555       1.737
LSTAT         -0.5489      0.047    -11.568      0.000      -0.642      -0.456
==============================================================================
Omnibus:                      170.253   Durbin-Watson:                   1.110
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              717.396
Skew:                           1.462   Prob(JB):                    1.66e-156
Kurtosis:                       8.047   Cond. No.                     1.26e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.26e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
"""


#VIF
y, X = dmatrices('PRICE ~ LCRIM + CRIM + ZN + INDUS + CHAS + NOX + RM + DIS + RAD + TAX + PTRATIO + LB + B + LSTAT + AGE', df, return_type='dataframe')
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(df.values, i) for i in range(X.shape[1])]
vif["feature"] = X.columns
vif
"""
    VIF Factor    feature
0     2.429128  Intercept
1     3.139628      LCRIM
2    14.698833       CRIM
3     1.176350         ZN
4    84.523755      INDUS
5   144.018814       CHAS
6    21.908891        NOX
7    15.952535         RM
8    21.510792        DIS
9    62.387602        RAD
10   98.771163        TAX
11   96.039159    PTRATIO
12   13.188982         LB
13   25.220560          B
14  280.679042      LSTAT
15    9.967548        AGE
"""



from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 170357387571136
"""