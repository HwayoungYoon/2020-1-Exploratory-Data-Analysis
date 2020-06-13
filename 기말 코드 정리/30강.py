# -*- coding: utf-8 -*-
"""
30강: 삼원분산분석, 데이터타입과 관측치, 그룹과 분석
"""


"""
삼원분산분석
"""
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "whitegrid")
df = sns.load_dataset("exercise")
sns.factorplot("time", "pulse", hue = "kind", col = "diet", 
               data = df, hue_order = ["rest", "walking", "running"],
               palette = "YlGnBu_d", aspect = .75).despine(left = True)


"""
관측치의 형태
"""
#Boolean
condition = False
if condition == True:
    print("OK")
else:
    print("Try again")

#String
str = "Female"
print("The String(", str, ") is of type", type(str))

#Numbers: int
num = 2
print("The number(", num, ") is of type", type(num))

#Numbers: float
num = 3.0
print("The number(", num, ") is of type", type(num))

#Numbers: complex
num = 3+5j
print("The number(", num, ") is of type", type(num))