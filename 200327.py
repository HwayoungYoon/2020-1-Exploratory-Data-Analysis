Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #리스트를 만들기 위해 대괄호를 사용한다.
>>> #len() 함수를 통해 리스트 내 원소의 수를 센다.
>>> #max() 함수와 min() 함수는 최대/최소 값을 찾는다.
>>> #count() 함수는 리스트 내 특정 값이 등장한 횟수를 센다.
>>> a_list = [1,2,3]
>>> another_list = ['printer',5,['star','circle
			     
SyntaxError: EOL while scanning string literal
>>> another_list = ['printer',5,['star','circle',9]]
>>> #리스트 분할
>>> print(a_list[0:2])
[1, 2]
>>> #리스트 복사
>>> a_new_list = a_list[:]
>>> print(a_new_list)
[1, 2, 3]
>>> #리스트 병합
>>> a_longer_list = a_list + another_list
>>> print(a_longer_list)
[1, 2, 3, 'printer', 5, ['star', 'circle', 9]]
>>> #in
>>> if 2 in a_list:
	print(a_list)

	
[1, 2, 3]
>>> #Append
>>> a_list.append(4)
>>> a_list
[1, 2, 3, 4]
>>> #pop: 위치 지정 삭제
>>> a_list.pop()
4
>>> a_list
[1, 2, 3]
>>> #remove: 숫자 지정 삭제
>>> a_list.remove(3)
>>> a_list
[1, 2]
>>> #reverse: 순서 변경
>>> a_list.reverse()
>>> a_list
[2, 1]
>>> #sorted 함수를 이용하여 리스트들의 특정 위치에 따라 리스트 정렬
>>> my_list = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]
>>> my_list_sorted_by_index_3 = sorted(my_list,key = lambda index_value: index_value[3])
>>> my_list_sorted_by_index_3
[[4, 3, 2, 1], [2, 4, 1, 3], [1, 2, 3, 4]]
>>> 
>>> #괄호를 사용하여 튜플 생성
>>> my_tuple = ('x','y','z')
>>> var1 = red
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    var1 = red
NameError: name 'red' is not defined
>>> var1 = 'red'
>>> var2 = 'robin'
>>> var1, var2 = var2, var1
>>> print(var1,var2)
robin red
>>> my_list = [1,2,3]
>>> print(tuple(my_list))
(1, 2, 3)
>>> print(list(my_tuple))
['x', 'y', 'z']
>>> #튜플 변경
>>> number1 = (1,2,3,4)
>>> number1[0] = 100
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    number1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> ###튜플은 변경 불가
>>> #튜플 삽입
>>> number1.append(7)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    number1.append(7)
AttributeError: 'tuple' object has no attribute 'append'
>>> ###튜플은 수정(삽입) 불가
>>> 
>>> #딕셔너리
>>> goals = {'통계':4.0, '수학':4.5, '미디어공학':4.5}
>>> print(goals)
{'통계': 4.0, '수학': 4.5, '미디어공학': 4.5}
>>> print(type(goals))
<class 'dict'>
