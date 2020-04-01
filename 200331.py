>>> #pandas install
>>> #cmd에서 python -m pip install pandas 실행


#CSV 입,출력 실습
import sys
import pandas as pd
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file, sep=',')
print(data_frame)
data_frame.to_csv(output_file, index=False)
#cmd창에서 python 200331_1.py eda.csv output_eda.csv 입력
#eda.csv 파일 입력, output_eda.csv 파일 출력


>>> #excel 실습
>>> #import libraries
>>> import pandas as pd
>>> import os
>>> #define directory name
>>> base_dir = 'C:/Python/Python37-32'
>>> excel_file = '2019_2_prod.xls'
>>> excel_dir = os.path.join(base_dir, excel_file)
>>> #excel statement
>>> df_from_excel = pd.read_excel(excel_dir,
			      sheet_name = 'Sheet1',
			      header = 2,
			      dtype = {'ID': str,
				       'Size': str,
				       'Amount': float},
			      index_col = 'ID',
			      na_values = 'NaN')
Traceback (most recent call last):
  File "<pyshell#24>", line 8, in <module>
    na_values = 'NaN')
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 304, in read_excel
    io = ExcelFile(io, engine=engine)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 824, in __init__
    self._reader = self._engines[engine](self._io)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_xlrd.py", line 20, in __init__
    import_optional_dependency("xlrd", extra=err_msg)
  File "C:\Python\Python37-32\lib\site-packages\pandas\compat\_optional.py", line 92, in import_optional_dependency
    raise ImportError(msg) from None
ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.
>>> #xlrd install 필요
>>> #cmd 창에서 python -m pip install xlrd 실행
>>> df_from_excel = pd.read_excel(excel_dir,
			      sheet_name = 'Sheet1',
			      header = 2,
			      dtype = {'ID': str,
				       'Size': str,
				       'Amount': float},
			      index_col = 'ID',
			      na_values = 'NaN')
Traceback (most recent call last):
  File "<pyshell#27>", line 8, in <module>
    na_values = 'NaN')
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 334, in read_excel
    **kwds,
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 888, in parse
    **kwds,
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 515, in parse
    output[asheetname] = parser.read(nrows=nrows)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1133, in read
    ret = self._engine.read(nrows)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 2465, in read
    index, columns = self._make_index(data, alldata, columns, indexnamerow)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1556, in _make_index
    index = self._get_simple_index(alldata, columns)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1588, in _get_simple_index
    i = ix(idx)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1583, in ix
    raise ValueError(f"Index {col} invalid")
ValueError: Index ID invalid
>>> df_from_excel = pd.read_excel(excel_dir,
			      sheet_name = 'Sheet1',
			      header = 2,
			      dtype = {'ID': str,
				       'Size': str,
				       'Amount': float},
			      index_col = 'ID')
Traceback (most recent call last):
  File "<pyshell#28>", line 7, in <module>
    index_col = 'ID')
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 334, in read_excel
    **kwds,
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 888, in parse
    **kwds,
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\excel\_base.py", line 515, in parse
    output[asheetname] = parser.read(nrows=nrows)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1133, in read
    ret = self._engine.read(nrows)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 2465, in read
    index, columns = self._make_index(data, alldata, columns, indexnamerow)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1556, in _make_index
    index = self._get_simple_index(alldata, columns)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1588, in _get_simple_index
    i = ix(idx)
  File "C:\Python\Python37-32\lib\site-packages\pandas\io\parsers.py", line 1583, in ix
    raise ValueError(f"Index {col} invalid")
ValueError: Index ID invalid
>>> df_from_excel = pd.read_excel(excel_dir,
			      sheet_name = 'Sheet1',
			      header = 2,
			      dtype = {'ID': str,
				       'Size': str,
				       'Amount': float})
>>> print(df_from_excel)
   10101002  M  20032
0  10101003  L   4120
1  10101004  E    105
2  10101005  E   1242
>>> df_from_excel = pd.read_excel(excel_dir,
			      sheet_name = 'Sheet1',
			      dtype = {'ID': str,
				       'Size': str,
				       'Amount': float})
>>> print(df_from_excel)
         ID Size   Amount
0  10101001    Y   6019.0
1  10101002    M  20032.0
2  10101003    L   4120.0
3  10101004    E    105.0
4  10101005    E   1242.0
>>> 
