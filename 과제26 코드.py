# -*- coding: utf-8 -*-

#library선언
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import glm
from statsmodels.genmod.families import Binomial

#데이터 불러오기
challenger = pd.read_csv("challenger_data.csv")

#요약 테이블 생성
df = pd.DataFrame()
df['temp'] = np.unique(challenger.Temperature)
df['failed'] = 0
df['ok'] = 0
df['total'] = 0
df.index = df.temp.values

#온도별 이륙 성공여부 체크
for ii in range(challenger.shape[0]):
    curTemp = challenger.Temperature[ii]
    curVal = challenger.Incident[ii]
    df.loc[curTemp,'total'] += 1
    if curVal == 1:
        df.loc[curTemp, 'failed'] += 1
    else:
        df.loc[curTemp, 'ok'] += 1 

#로지스틱 모델링
model = glm("failed ~ temp", data = df, family = Binomial()).fit()
print(model.summary())
"""
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:                 failed   No. Observations:                   17
Model:                            GLM   Df Residuals:                       15
Model Family:                Binomial   Df Model:                            1
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                   -inf
Date:                Fri, 12 Jun 2020   Deviance:                       91.192
Time:                        12:30:34   Pearson chi2:                     22.0
No. Iterations:                     6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     14.4216      7.547      1.911      0.056      -0.369      29.213
temp          -0.2130      0.109     -1.956      0.051      -0.426       0.000
==============================================================================
"""

fig = plt.figure()
sns.lmplot(x = "Temperature", y = "Incident", data = challenger, logistic = True)
plt.title("Defects of the Space Shuttle O-Rings vs temperatue", position = (0.5, 1.0+0.05), fontsize = 15)
plt.xlabel('Outside Temperature[F]')
plt.ylabel('Demage Incident')


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 228126258343324
"""