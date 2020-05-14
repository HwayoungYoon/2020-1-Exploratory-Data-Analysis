# -*- coding: utf-8 -*-


#import library
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial


#데이터 load
titanic = sns.load_dataset("titanic")
titanic.info
"""
<bound method DataFrame.info of      survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0           0       3    male  22.0  ...   NaN  Southampton     no  False
1           1       1  female  38.0  ...     C    Cherbourg    yes  False
2           1       3  female  26.0  ...   NaN  Southampton    yes   True
3           1       1  female  35.0  ...     C  Southampton    yes  False
4           0       3    male  35.0  ...   NaN  Southampton     no   True
..        ...     ...     ...   ...  ...   ...          ...    ...    ...
886         0       2    male  27.0  ...   NaN  Southampton     no   True
887         1       1  female  19.0  ...     B  Southampton    yes   True
888         0       3  female   NaN  ...   NaN  Southampton     no  False
889         1       1    male  26.0  ...     C    Cherbourg    yes   True
890         0       3    male  32.0  ...   NaN   Queenstown     no   True

[891 rows x 15 columns]>
"""


#결측치
titanic_age = titanic[titanic["age"].isna()]
titanic0 = titanic.drop(titanic_age.index)

my_formula = 'age ~ pclass + sibsp + adult_male + survived'
lm = ols(my_formula, data=titanic0).fit()
print(lm.summary())
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    age   R-squared:                       0.285
Model:                            OLS   Adj. R-squared:                  0.281
Method:                 Least Squares   F-statistic:                     70.68
Date:                Thu, 14 May 2020   Prob (F-statistic):           2.21e-50
Time:                        13:04:43   Log-Likelihood:                -2803.5
No. Observations:                 714   AIC:                             5617.
Df Residuals:                     709   BIC:                             5640.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
======================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------
Intercept             46.3895      2.027     22.882      0.000      42.409      50.370
adult_male[T.True]     5.2059      1.221      4.263      0.000       2.808       7.603
pclass                -7.2739      0.595    -12.230      0.000      -8.442      -6.106
sibsp                 -3.5523      0.538     -6.609      0.000      -4.608      -2.497
survived              -3.9669      1.241     -3.197      0.001      -6.403      -1.531
==============================================================================
Omnibus:                       25.801   Durbin-Watson:                   1.926
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               27.622
Skew:                           0.466   Prob(JB):                     1.00e-06
Kurtosis:                       3.242   Cond. No.                         14.3
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""

titanic_age['age'] = lm.predict(titanic_age)
titanic1 = pd.concat([titanic0, titanic_age])
missing = titanic1.isnull().sum()

model1 = glm("survived ~ deck", data=titanic1, family=Binomial()).fit()
print(model1.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:               survived   No. Observations:                  203
Model:                            GLM   Df Residuals:                      196
Model Family:                Binomial   Df Model:                            6
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -124.64
Date:                Thu, 14 May 2020   Deviance:                       249.27
Time:                        13:04:50   Pearson chi2:                     203.
No. Iterations:                     4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -0.1335      0.518     -0.258      0.796      -1.148       0.881
deck[T.B]      1.2040      0.616      1.954      0.051      -0.004       2.412
deck[T.C]      0.5108      0.581      0.879      0.380      -0.629       1.650
deck[T.D]      1.2730      0.658      1.935      0.053      -0.017       2.562
deck[T.E]      1.2321      0.659      1.869      0.062      -0.060       2.524
deck[T.F]      0.6035      0.770      0.784      0.433      -0.906       2.113
deck[T.G]      0.1335      1.126      0.119      0.906      -2.073       2.340
==============================================================================
"""

titanic1['deck'].replace({'B':1, 'D':1, 'E':1}, inplace=True)
titanic1['deck'].replace({'A':0, 'C':0, 'F':0, 'G':0}, inplace=True)
titanic1.deck.fillna(0, inplace=True)

titanic1['sex'] = np.where(titanic1.sex == "female", 1, 0)
titanic1['alone'] = np.where(titanic1.alone == "True", 1, 0)

pd.crosstab(titanic1.deck, "columns")
"""
col_0  columns
deck          
0.0        779
1.0        112
"""

model2 = glm("survived ~ deck", data=titanic1, family=Binomial()).fit()
print(model2.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:               survived   No. Observations:                  891
Model:                            GLM   Df Residuals:                      889
Model Family:                Binomial   Df Model:                            1
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -557.66
Date:                Thu, 14 May 2020   Deviance:                       1115.3
Time:                        13:05:07   Pearson chi2:                     891.
No. Iterations:                     4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -0.7028      0.076     -9.232      0.000      -0.852      -0.554
deck           1.8014      0.231      7.794      0.000       1.348       2.254
==============================================================================
"""


#상관계수 plot
plt.figure(figsize=(15,15))
sns.heatmap(titanic1.corr(), annot=True, fmt='.2f', cmap='Blues')
plt.tick_params(labelsize=13)
plt.title("Correlations of Titanic data", position=(0.5, 1.0+0.05), fontsize=15)


#pair plot
num_cols = ["age", "alone", "sex", "deck", "pclass", "fare"]
sns.pairplot(titanic1, hue='survived', x_vars=num_cols, y_vars=titanic['survived'])


#데이터셋 분할
train = titanic1.sample(frac=0.7, random_state=1234)
test = titanic1.drop(train.index)


#ANOVA
model3 = glm("survived ~ age + alone + sex + deck + pclass", data=train, family=Binomial()).fit()
print(model3.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:               survived   No. Observations:                  624
Model:                            GLM   Df Residuals:                      619
Model Family:                Binomial   Df Model:                            4
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -280.08
Date:                Thu, 14 May 2020   Deviance:                       560.16
Time:                        13:05:45   Pearson chi2:                     643.
No. Iterations:                     5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      1.9610      0.534      3.670      0.000       0.914       3.008
age           -0.0334      0.009     -3.841      0.000      -0.050      -0.016
alone      -1.861e-14   1.95e-15     -9.553      0.000   -2.24e-14   -1.48e-14
sex            2.4905      0.226     11.001      0.000       2.047       2.934
deck           0.5962      0.374      1.596      0.111      -0.136       1.328
pclass        -1.1371      0.163     -6.974      0.000      -1.457      -0.818
==============================================================================
"""


#모델 평가_predict
test["predict"] = model3.predict(test)


#모델 평가_confusion matrix creation
preds = np.where(test.predict > 0.5, 1, 0)
pd.crosstab(test.survived, preds)
"""
col_0       0   1
survived         
0         142  19
1          26  80
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 141991317885390
"""