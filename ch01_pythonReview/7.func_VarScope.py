# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:06:21 2019

@author: shkim
"""

def calculate(x, y):
    total = x + y   # 지역 변수 
    print("calculation--> a:", str(a), "b:", str(b), "a + b:", str(a+b), "total:", str(total))
#    print("calculation--> a:{0}, b:{1}, a+b:{2}, total:{3}".format(str(a), str(b), str(a+b), str(total)))
    return total

a = 5                               # a와 b는 전역 변수
b = 7
total = 0                           # 전역 변수 total
print("main--> a:", str(a), "b:", str(b), "a + b:", str(a+b), "total:", str(total))

sum = calculate (a, b)
print("After Calculation-->total:", str(total), " sum:", str(sum)) # 지역 변수는 전역 변수에 영향을 주지 않음

#%%
def f():
    global s
    s = "I love London!"
    print(s)

s = "I love Paris!"
f()
print(s)

