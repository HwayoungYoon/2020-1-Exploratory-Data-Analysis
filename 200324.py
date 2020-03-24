Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> #오늘의 날짜와 년, 월, 일 요소들을 출력하기
>>> today = datetime.date.today()
>>> #41
>>> print("today: {0!s}".format(today))
today: 2020-03-24
>>> #42
>>> print("{0!s}".format(today.year))
2020
>>> #43
>>> print("{0!s}".format(today.month))
3
>>> #44
>>> print("{0!s}".format(today.day))
24
>>> 
>>> #날짜의 년, 월, 일 출력하기
>>> d = datetime.date(2020,03,16)
SyntaxError: invalid token
>>> d = datetime.date(2020,3,16)
>>> print("{0}년 {1}월 {2}일".format(d.year,d.month,d.day))
2020년 3월 16일
>>> 
>>> #sort() 함수를 이용하여 리스트 정렬
>>> unsorted_list = [3,5,1,7,2,8,4,9,0,6]
>>> #88
>>> print("{}".format(unsorted_list))
[3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
>>> list_copy = unsorted_list[:]
>>> list_copy.sort()
>>> #89
>>> print("{}".format(list_copy))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print("{}".format(unsorted_list))
[3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
>>> 
>>> #if-else 조건문
>>> #124
>>> x = 5
>>> if x > 4 or x != 9:
	print("{}".format(x))
	else:
		
SyntaxError: invalid syntax
>>> if x > 4 or x != 9:
	print("{}".format(x))
	else:
	print("x is not greater than 4")
	
SyntaxError: invalid syntax
>>> if x > 4 or x != 9:
	print("{}".format(x))
else:
print("x is not greater than 4")
SyntaxError: expected an indented block
>>> if x > 4 or x != 9:
	print("{}".format(x))
else:
	print("x is not greater than 4")

	
5
>>> 
>>> #if-elif-else 조건문
>>> coffee = 3
>>> money = int(input('돈을 넣어 주세요:'))
돈을 넣어 주세요:
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    money = int(input('돈을 넣어 주세요:'))
ValueError: invalid literal for int() with base 10: ''
>>> moca = 100
>>> hotchoco = 150
>>> while True:
	if coffee >=1:
		choice = int(input('마시고 싶은 커피를 선택하세요\n1.모카\n2.핫초코\n'))
		print(str(choice)+'를 선택했습니다.')
		if choice == 1 and money >= moca:
			print('모카 커피가 나왔습니다.')
			coffee -= 1
			money =- moca
		elif choice == 2 and money >= hotchoco:
			print('핫초코가 나왔습니다')
			coffee -= 1
			money -= hotchoco
		elif money < hotchoco or money <= moca:
			print('잔돈이 부족합니다')
		else:
			print('없는 메뉴입니다.')
			continue
		print('잔돈은' + str(money) + '원 입니다.')
		choice = str(input('거스름돈을 받으려면 q를 누르고 계속 진행하려면 다른 키를 입력해주세요'))
		if choice == 'q':
			print('잔돈' + str(money) + '원이 나왔습니다.')
			break
	else:
		print('커피가 부족합니다.')
		break

	
마시고 싶은 커피를 선택하세요
1.모카
2.핫초코
2
2를 선택했습니다.
Traceback (most recent call last):
  File "<pyshell#69>", line 9, in <module>
    elif choice == 2 and money >= hotchoco:
NameError: name 'money' is not defined
>>> while True:
	if coffee >=1:
		choice = int(input('마시고 싶은 커피를 선택하세요\n1.모카\n2.핫초코\n'))
		money = int(input('돈을 넣어 주세요:'))
		print(str(choice)+'를 선택했습니다.')
		if choice == 1 and money >= moca:
			print('모카 커피가 나왔습니다.')
			coffee -= 1
			money =- moca
		elif choice == 2 and money >= hotchoco:
			print('핫초코가 나왔습니다')
			coffee -= 1
			money -= hotchoco
		elif money < hotchoco or money <= moca:
			print('잔돈이 부족합니다')
		else:
			print('없는 메뉴입니다.')
			continue
		print('잔돈은' + str(money) + '원 입니다.')
		choice = str(input('거스름돈을 받으려면 q를 누르고 계속 진행하려면 다른 키를 입력해주세요'))
		if choice == 'q':
			print('잔돈' + str(money) + '원이 나왔습니다.')
			break
	else:
		print('커피가 부족합니다.')
		break

	
마시고 싶은 커피를 선택하세요
1.모카
2.핫초코
2
돈을 넣어 주세요:200
2를 선택했습니다.
핫초코가 나왔습니다
잔돈은50원 입니다.
거스름돈을 받으려면 q를 누르고 계속 진행하려면 다른 키를 입력해주세요q
잔돈50원이 나왔습니다.
>>> 
>>> for 조건문
SyntaxError: invalid syntax
>>> #for 조건문
>>> y = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
>>> z = ['Annie','Betty','Claire','Daphine','Ellie','Franchesca','Greta','Holly','Isabel','Jenny']
>>> #126
>>> for month in y:
	print("{!s}".format(month))

	
Jan
Feb
Mar
Apr
Jun
Jul
Aug
Sep
Oct
Nov
Dec
>>> #127
>>> print("(Index value: name in list)")
(Index value: name in list)
>>> for i in range(len(z)):
	print("{0!s}:{1!s}".format(i,z[i]))

	
0:Annie
1:Betty
2:Claire
3:Daphine
4:Ellie
5:Franchesca
6:Greta
7:Holly
8:Isabel
9:Jenny
>>> #128
>>> print("(access elements in y wiht z's index values)")
(access elements in y wiht z's index values)
>>> for j in range(len(z)):
	if y[j].startswith('J'):
		print("{!s}".format(y[j]))

		
Jan
Jun
Jul
>>> 
>>> #Break, Continue
>>> i = 0
>>> while True:
	print(i)
	i += 1
	if i == 100:
		break

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> for i in (100):
	if i % 2 == 0:
		continue
print(i)
SyntaxError: invalid syntax
>>> for i in (100):
	if i % 2 == 0:
		continue
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    for i in (100):
TypeError: 'int' object is not iterable
>>> for i in (100):
	if i % 2 == 0:
		continue
	print([i])

	
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    for i in (100):
TypeError: 'int' object is not iterable
>>> for i in (100):
	if i%2 == 0:
		continue
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    for i in (100):
TypeError: 'int' object is not iterable
>>> for i in 100:
	if i % 2 == 0:
		continue
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    for i in 100:
TypeError: 'int' object is not iterable
>>> for i in int(100):
	if i % 2 == 0:
		continue
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    for i in int(100):
TypeError: 'int' object is not iterable
>>> for i in range(100):
	if i % 2 == 0:
		continue
	print(i)

	
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
>>> #오류해결 참고(https://www.codecademy.com/forum_questions/54f231c876b8fe4269002f2f)
>>> 
>>> #파일 읽기
>>> import sys
>>> #139
>>> input_file = sys.argv[1]
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    input_file = sys.argv[1]
IndexError: list index out of range
>>> input_file = sys.argv[1]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    input_file = sys.argv[1]
IndexError: list index out of range
>>> print("Output #139: ")
Output #139: 
>>> input_file = sys.argv[1]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    input_file = sys.argv[1]
IndexError: list index out of range
>>> python file_to_read.py
SyntaxError: invalid syntax
>>> 
