Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> d_date = "2020/03/18"
>>> d = datetime.strptime(d_date, '%Y/%m/%d')
>>> print("{0}년 {1}월 {2}일".format(d.year,d.month,d.day))
2020년 3월 18일
>>> 
>>> from uuid import getnode as get_mac
>>> mac = get_mac()
>>> print("Mac address : {0}".format(mac))
Mac address : 150075731951663
>>> 
