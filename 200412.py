>>> #히스토그램
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> import pandas as pd
>>> 
>>> x = np.random.normal(size=1000)
>>> sns.distplot(x, bins=20, kde=True, rug=True, label="Histogram w/o density")
<matplotlib.axes._subplots.AxesSubplot object at 0x0B03A790>
>>> sns.utils.axlabel("Value","Frequency")
>>> plt.title("Histogram of a Random sample from a Normal distribution")
Text(0.5, 1.0, 'Histogram of a Random sample from a Normal distribution')
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0ADA75D0>
>>> plt.savefig('histogram_distplot.png', dpi=400, bbox_inches='tight')
>>> plt.show()
>>> 
>>> #교차표
>>> import pandas as pd
>>> import seaborn as sns
>>> from scipy.stats import chi2_contingency
>>> #Titanic 데이터 가져오기
>>> titanic = sns.load_dataset("titanic")
>>> titanic
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
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

[891 rows x 15 columns]
>>> #NaN 없애기
>>> mean = titanic['age'].mean()
>>> titanic['age'].fillna(mean, inplace=True)
>>> #age 분할
>>> titanic['age_cut'] = pd.cut(titanic['age'],
			    bins=[10,20,30,40,50,60,70,80],
			    labels=['10대','20대','30대','40대','50대','60대','70대'])
>>> #교차표 생성
>>> crosstab_survived_age = pd.crosstab(titanic['survived'],titanic['age_cut'])
>>> crosstab_survived_age
age_cut   10대  20대  30대  40대  50대  60대  70대
survived                                   
0          71  271   86   53   25   13    4
1          44  136   69   33   17    4    1
>>> #카이제곱 검정
>>> chi2, p, dof, ex = chi2_contingency(crosstab_survived_age)
>>> print("""Chi-square:""", chi2)
Chi-square: 8.31105934455244
>>> print("""P-value:""", p)
P-value: 0.21618849062981324
>>> 
