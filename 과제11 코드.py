# -*- coding: utf-8 -*-


#1번
import pandas as pd
import seaborn as sns

iris = sns.load_dataset("iris")
print(iris)
"""
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
"""

iris.groupby("species").mean()
"""
            sepal_length  sepal_width  petal_length  petal_width
species                                                         
setosa             5.006        3.428         1.462        0.246
versicolor         5.936        2.770         4.260        1.326
virginica          6.588        2.974         5.552        2.026
"""


#2번
import pandas as pd

df1 = pd.DataFrame({'이름':['박가나','이다라','김마바','최사아','김자차'],
                   '학번':['180832','180799','180801','180924','180900']})
df2 = pd.DataFrame({'학번':['180832','180799','180801','180924','180900'],
                    '주소':['서울 도봉구','서울 강북구','서울 용산구','경기 부천시','인천 부평구']})

df_merge = pd.merge(df1, df2)
print(df_merge)
"""
    이름      학번      주소
0  박가나  180832  서울 도봉구
1  이다라  180799  서울 강북구
2  김마바  180801  서울 용산구
3  최사아  180924  경기 부천시
4  김자차  180900  인천 부평구
"""


from uuid import getnode as get_mac
mac = get_mac()
print("Mac address: {0}".format(mac))
"""
Mac address: 247479321436448
"""



