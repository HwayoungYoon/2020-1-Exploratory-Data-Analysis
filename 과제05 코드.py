Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
>>> import pandas as pd
>>> df=pd.read_csv('C:\Python\Python37-32\supplier_data.csv')
>>> print(df.columns)
Index(['Supplier Name', ' Invoice Number', ' Part Number', ' Cost',
       ' Purchase Date'],
      dtype='object')
>>> df[' Cost']=df[' Cost'].str.strip("$").astype(float)
>>> df_new=df[df['Supplier Name'].str.contains('X')]
>>> print(df_new[' Cost'].mean())
625.0
>>> 
>>> #2
>>> df_col=df[['Supplier Name',' Purchase Date']]
>>> df_col.shape[0]
12
>>> df_col.shape[1]
2
>>> 
>>> from uuid import getnode as get_mac
>>> mac = get_mac()
>>> print(" Mac address : {0}".format(mac))
 Mac address : 150075731951663
>>> 
