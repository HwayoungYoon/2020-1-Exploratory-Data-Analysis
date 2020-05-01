Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1번
>>> A = [1,3,4,2,5]
>>> B = sorted(A)
>>> B.remove(5)
>>> B.append(6)
>>> print(B)
[1, 2, 3, 4, 6]
>>> 
>>> #2번
>>> tuple1 = (1,2,3,4)
>>> tuple2 = list(tuple1)
>>> tuple2.append(5)
>>> tuple1_add = tuple(tuple2)
>>> print(tuple1_add)
(1, 2, 3, 4, 5)
>>> 
>>> from uuid import getnode as get_mac
>>> mac = get_mac()
>>> print(" Mac address : {0}".format(mac))
 Mac address : 150075731951663
>>> 
