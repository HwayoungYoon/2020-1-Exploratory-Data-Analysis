##정수 및 실수 실습

x=9
#4 정수
print("Output #4: {0}".format(x))
print("{0}".format(x))
#5
print("{0}".format(3**4))
#6 실수
print("{0}".format(int(8.3)/int(2.7)))
#7
print("{0:.3f}".format(8.3/2.7))
y=2.5*4.8
#8
print("{0:.1f}".format(y))
r=8/float(3)
#9
print("{0:.2f}".format(r))
#10
print("{0:.4f}".format(8.0/3))



##math 모듈함수 실습

#from(라이브러리) import(특정함수)
from math import exp, log, sqrt
#11 지수
print("{0:.4f}".format(exp(3)))
#12
print("{0:.2f}".format(log(4)))
#13
print("{0:.1f}".format(sqrt(81)))



#이진형 데이터 실습

a=2>1
a
b=2<1
b
type(a)



#군집형(문자열) 데이터 실습

#14 특수문자 사용
print("{0:s}".format('I\'m enjoying learning Python.'))
#15 문자열 길이 조정
print("{0:s}".format("This is a long string. Without the backslash \
it would run off the page on the right in the text editor and be very \
difficult to read and edit. By using the backslash you can split the long \
string into smaller strings on separate lines so that the whole string is easy \
to view in the text editor."))
#16 여러 라인의 문자열 출력
print("{0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))
#17
print("{0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))

#문자열 병합
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
#18 문자열 연산자
print("{0:s}".format(sentence))
#19
print("{0:s}{1:s}{2:s}".format("She is ","very "*4,"beautiful."))
m = len(sentence)
#20
print("{0:d}".format(m))

#문자열 분리
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
#21 공백으로 분리
print("{0}".format(string1_list1))
#22
print("FIRST PRICE:{0} SECOND PRICE:{1} THIRD PRICE:{2}"\
      .format(string1_list2[0], string1_list2[1], string1_list2[2]))
string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
#23 쉼표로 분리
print("{0}".format(string2_list))
#24
print("{0} {1} {2}".format(string2_list[1], string2_list[5],\
                           string2_list[-1]))

# 문자열 정의
string3 = " Remove unwanted characters from this string.\t\t         \n"
#26
print("string3: {0:s}".format(string3))
#왼쪽 스트립
string3_lstrip = string3.lstrip()
#27
print("lstrip: {0:s}".format(string3_lstrip))
#오른쪽 스트립
string3_rstrip = string3.rstrip()
#28
print("rstrip: {0:s}".format(string3_rstrip))
#양쪽 스트립
string3_strip = string3.strip()
#29
print("strip: {0:s}".format(string3_strip))
