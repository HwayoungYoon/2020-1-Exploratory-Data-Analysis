# -*- coding: utf-8 -*-
"""
39강: 3차원 플롯, 로지스틱 회귀
"""


"""
3차원 플롯 프로그램
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.linspace(-5, 5, 101)
(X, Y) = np.meshgrid(x, x)

np.random.seed(987654321)
Z = -5 + 3*X - 0.5*Y + np.random.randn(np.shape(X)[0], np.shape(X)[1])
myCmap = cm.GnBu_r

fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(X, Y, Z, cmap = myCmap, rstride = 2, cstride = 2,
                       linewidth = 0, antialiased = False)
ax.view_init(20, -120)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.colorbar(surf, shrink = 0.6)
plt.title("3D plot", position = (0.5, 1.0+0.05), fontsize = 15)


"""
로지스틱 회귀
"""
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

fig = plt.figure()
sns.lmplot(x = "Temperature", y = "Incident", data = challenger, logistic = True)
plt.title("Defects of the Space Shuttle O-Rings vs temperatue", position = (0.5, 1.0+0.05), fontsize = 15)
plt.xlabel('Outside Temperature[F]')
plt.ylabel('Demage Incident')