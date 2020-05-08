# -*- coding: utf-8 -*-

#library import
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial


#데이터 가져오기
crabs = pd.read_csv("horseshoe.csv")


#일반적인 통계량 확인
crabs.describe().unstack()
"""
color        count     173.000000
             mean        3.439306
             std         0.801933
             min         2.000000
             25%         3.000000
             50%         3.000000
             75%         4.000000
             max         5.000000
spine        count     173.000000
             mean        2.485549
             std         0.825516
             min         1.000000
             25%         2.000000
             50%         3.000000
             75%         3.000000
             max         3.000000
width        count     173.000000
             mean       26.298844
             std         2.109061
             min        21.000000
             25%        24.900000
             50%        26.100000
             75%        27.700000
             max        33.500000
satellite    count     173.000000
             mean        2.919075
             std         3.148336
             min         0.000000
             25%         0.000000
             50%         2.000000
             75%         5.000000
             max        15.000000
weight       count     173.000000
             mean     2437.190751
             std       577.025214
             min      1200.000000
             25%      2000.000000
             50%      2350.000000
             75%      2850.000000
             max      5200.000000
weight_1     count     173.000000
             mean        2.437191
             std         0.577025
             min         1.200000
             25%         2.000000
             50%         2.350000
             75%         2.850000
             max         5.200000
satellite_1  count     173.000000
             mean        0.641618
             std         0.480917
             min         0.000000
             25%         0.000000
             50%         1.000000
             75%         1.000000
             max         1.000000
dtype: float64
"""


#빈도수 확인, 로지스틱 곡선 plot 생성
sns.countplot(x='satellite_1', data=crabs)
sns.regplot(x='width', y='satellite_1', data=crabs, logistic=True)


#color, spine 빈도표
pd.crosstab(crabs.color, "count")
"""
col_0  count
color       
2         12
3         95
4         44
5         22
"""

pd.crosstab(crabs.spine, "count")
"""
col_0  count
spine       
1         37
2         15
3        121
"""


#로지스틱 회귀
model = glm('satellite_1 ~ width', data=crabs, family=Binomial()).fit()
print(model.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      171
Model Family:                Binomial   Df Model:                            1
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -97.226
Date:                Wed, 06 May 2020   Deviance:                       194.45
Time:                        14:21:16   Pearson chi2:                     165.
No. Iterations:                     4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    -12.3508      2.629     -4.698      0.000     -17.503      -7.199
width          0.4972      0.102      4.887      0.000       0.298       0.697
==============================================================================
"""


#예측
crabs["predict"] = model.predict(crabs.width)
crabs.head()
"""
   color  spine  width  satellite  weight  weight_1  satellite_1   predict
0      3      3   28.3          8    3050      3.05            1  0.848233
1      4      3   22.5          0    1550      1.55            0  0.238099
2      2      1   26.0          9    2300      2.30            1  0.640418
3      4      3   24.8          0    2100      2.10            0  0.495125
4      4      3   26.0          4    2600      2.60            1  0.640418
"""


#예측 성능 확인
preds = np.where(crabs.predict > 0.5, 1, 0)
pd.crosstab(preds, crabs.satellite_1)
"""
satellite_1   0   1
row_0              
0            27  16
1            35  95
"""


#다변량 로지스틱 회귀
model2 = glm('satellite_1 ~ width + C(color) + weight_1', data=crabs, family=Binomial()).fit()
print(model2.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            satellite_1   No. Observations:                  173
Model:                            GLM   Df Residuals:                      167
Model Family:                Binomial   Df Model:                            5
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -93.106
Date:                Wed, 06 May 2020   Deviance:                       186.21
Time:                        15:24:02   Pearson chi2:                     170.
No. Iterations:                     5                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          z      P>|z|      [0.025      0.975]
---------------------------------------------------------------------------------
Intercept        -8.6445      3.770     -2.293      0.022     -16.034      -1.255
C(color)[T.3]     0.1310      0.742      0.177      0.860      -1.323       1.585
C(color)[T.4]    -0.1610      0.780     -0.206      0.836      -1.690       1.368
C(color)[T.5]    -1.2453      0.855     -1.456      0.145      -2.922       0.431
width             0.2906      0.190      1.528      0.126      -0.082       0.663
weight_1          0.7727      0.698      1.107      0.268      -0.595       2.140
=================================================================================
"""