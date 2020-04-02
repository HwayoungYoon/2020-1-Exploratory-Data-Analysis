>>> import pandas as pd
>>> df=pd.read_csv('supplier_data.csv')
>>> print(df)
   Supplier Name  Invoice Number   Part Number  Cost  Purchase Date
0     Supplier X        001-1001          2341  $500        1/20/14
1     Supplier X        001-1001          2341  $500        1/20/14
2     Supplier X        001-1001          5467  $750        1/20/14
3     Supplier X        001-1001          5467  $750        1/20/14
4     Supplier Y         50-9501          7009  $250        1/30/14
5     Supplier Y         50-9501          7009  $250        1/30/14
6     Supplier Y         50-9505          6650  $125         2/3/14
7     Supplier Y         50-9505          6650  $125         2/3/14
8     Supplier Z        920-4803          3321  $615         2/3/14
9     Supplier Z        920-4804          3321  $615        2/10/14
10    Supplier Z        920-4805          3321  $615        2/17/14
11    Supplier Z        920-4806          3321  $615        2/24/14
>>> #조건을 만족하는 행 가져오기
>>> print(df.columns)
Index(['Supplier Name', ' Invoice Number', ' Part Number', ' Cost',
       ' Purchase Date'],
      dtype='object')
>>> df[' Cost']=df[' Cost'].str.strip("$").astype(float)
>>> df_new=df[(df['Supplier Name'].str.contains('Z'))|(df[' Cost']>600.0)]
>>> df_new
   Supplier Name  Invoice Number   Part Number   Cost  Purchase Date
2     Supplier X        001-1001          5467  750.0        1/20/14
3     Supplier X        001-1001          5467  750.0        1/20/14
8     Supplier Z        920-4803          3321  615.0         2/3/14
9     Supplier Z        920-4804          3321  615.0        2/10/14
10    Supplier Z        920-4805          3321  615.0        2/17/14
11    Supplier Z        920-4806          3321  615.0        2/24/14
>>> important_dates=['1/20/14','1/30/14']
>>> df_value_in_set=df[df[' Purchase Date'].isin(important_dates)]
>>> print(df_value_in_set)
  Supplier Name  Invoice Number   Part Number   Cost  Purchase Date
0    Supplier X        001-1001          2341  500.0        1/20/14
1    Supplier X        001-1001          2341  500.0        1/20/14
2    Supplier X        001-1001          5467  750.0        1/20/14
3    Supplier X        001-1001          5467  750.0        1/20/14
4    Supplier Y         50-9501          7009  250.0        1/30/14
5    Supplier Y         50-9501          7009  250.0        1/30/14
>>> #조건을 만족하는 열 가져오기
>>> import pandas as pd
>>> df=pd.read_csv('supplier_data.csv')
>>> df_column_by_index=df.iloc[:,0:3]
>>> df_column_by_name=df[[' Invoice Number',' Purchase Date']]
>>> print(df_column_by_index)
   Supplier Name  Invoice Number   Part Number
0     Supplier X        001-1001          2341
1     Supplier X        001-1001          2341
2     Supplier X        001-1001          5467
3     Supplier X        001-1001          5467
4     Supplier Y         50-9501          7009
5     Supplier Y         50-9501          7009
6     Supplier Y         50-9505          6650
7     Supplier Y         50-9505          6650
8     Supplier Z        920-4803          3321
9     Supplier Z        920-4804          3321
10    Supplier Z        920-4805          3321
11    Supplier Z        920-4806          3321
>>> print(df_column_by_name)
    Invoice Number  Purchase Date
0         001-1001        1/20/14
1         001-1001        1/20/14
2         001-1001        1/20/14
3         001-1001        1/20/14
4          50-9501        1/30/14
5          50-9501        1/30/14
6          50-9505         2/3/14
7          50-9505         2/3/14
8         920-4803         2/3/14
9         920-4804        2/10/14
10        920-4805        2/17/14
11        920-4806        2/24/14
>>> #행과 열의 수 세기
>>> #행의 수 세기
>>> len(df)
12
>>> df.shape[0]
12
>>> len(df.index)
12
>>> #열의 수 세기
>>> df.shape[1]
5
>>> len(df.columns)
5
>>> #Null값이 아닌 행 개수 세기
>>> df.count()
Supplier Name      12
 Invoice Number    12
 Part Number       12
 Cost              12
 Purchase Date     12
dtype: int64
>>> #평균,분산 등 계산하기
>>> df[' Cost']=df[' Cost'].str.strip("$").astype(float)
>>> print(df)
   Supplier Name  Invoice Number   Part Number   Cost  Purchase Date
0     Supplier X        001-1001          2341  500.0        1/20/14
1     Supplier X        001-1001          2341  500.0        1/20/14
2     Supplier X        001-1001          5467  750.0        1/20/14
3     Supplier X        001-1001          5467  750.0        1/20/14
4     Supplier Y         50-9501          7009  250.0        1/30/14
5     Supplier Y         50-9501          7009  250.0        1/30/14
6     Supplier Y         50-9505          6650  125.0         2/3/14
7     Supplier Y         50-9505          6650  125.0         2/3/14
8     Supplier Z        920-4803          3321  615.0         2/3/14
9     Supplier Z        920-4804          3321  615.0        2/10/14
10    Supplier Z        920-4805          3321  615.0        2/17/14
11    Supplier Z        920-4806          3321  615.0        2/24/14
>>> print(df[' Cost'].sum())
5710.0
>>> print(df[' Cost'].mean())
475.8333333333333
>>> print(df[' Cost'].var())
52467.42424242424
>>> print(df[' Cost'].std())
229.05768758639
