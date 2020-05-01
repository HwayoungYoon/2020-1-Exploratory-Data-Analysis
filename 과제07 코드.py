Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #라이브러리 import
>>> import pandas as pd
>>> import seaborn as sns
>>> from scipy.stats import chi2_contingency
>>> 
>>> #iris 데이터 가져오기
>>> iris = sns.load_dataset("iris")
>>> iris
     sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

[150 rows x 5 columns]
>>> 
>>> #sepal_length 분할
>>> iris['sepal_len'] = pd.cut(iris['sepal_length'],
			   bins=[4,5,6,7,8],
			   labels=['len_4','len_5','len_6','len_7'])
>>> 
>>> #교차표 생성
>>> crosstab_sepal_len = pd.crosstab(iris['species'],iris['sepal_len'])
>>> crosstab_sepal_len
sepal_len   len_4  len_5  len_6  len_7
species                               
setosa         28     22      0      0
versicolor      3     27     20      0
virginica       1      8     29     12
>>> 
>>> #카이제곱 검정
>>> chi2, p, dof, ex = chi2_contingency(crosstab_sepal_len)
>>> print("""Chi-square:""", chi2)
Chi-square: 103.62761815252416
>>> print("""P-value:""", p)
P-value: 4.3870167312639317e-20
>>> 
>>> 
>>> 
>>> from uuid import getnode as get_mac
>>> mac = get_mac()
>>> print(" Mac address : {0}".format(mac))
 Mac address : 150075731951663
>>> 
