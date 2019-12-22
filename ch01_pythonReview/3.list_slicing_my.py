# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:26:37 2019

@author: shkim
"""

#%%
# Slicing Basic - List 분할
myl = [10, 20, 30, 40, 50, 60]
print(myl[:2])  # 2번 인덱스에서 분할
print(myl[2:])
print(myl[:3])  # 3번 인덱스에서 분할
print(myl[3:])

print(myl[3:5])

#%%
# 슬라이스 객체  s[start:stop:step]
# seq[start:stop:step]을 해석하기 위해 파이썬은 seq.__getitem__(slice(start, stop, step))을 호출한다.
s = 'bicycle'
print('1)', s[::])
print('2)', s[::1])
print('3)', s[::3])
print('4)', s[::-1])
print('5)', s[::-2])
print('6)', s[1:5:])
print('7)', s[4:0:-1])
print('8)', s[-3:-7:-1])

#%%
# 함수인자와 생략기호(ellipsis)

def f1(a, b, c, d, e):
    return a+c+e
#    return (a+b+c+d+e)  # error

print(f1(10, ..., 30, ..., 50))
#print(f1(10, 20, 30, 40, 50))
#print(f1(10, ...))  #error


def f1(a=1, b=2, c=3, d=4, e=5):
    return a+c+e
#    return (a+b+c+d+e)  # error

print(f1(10, ..., 30, ..., 50))
#print(f1(10, ...))  # ok, b가 생략됨
#print(f1(10))  # ok, b,c,d,e가 생략됨


#%%
# 다차원 슬라이싱과 생략기호(ellipsis)

myl = [[1,1,1], [2,2,2]]
print(myl)

myl = [[1,1,1], [...]]
print(myl)

myl = [[1,1,1], [2,...,2]]
print(myl)

#%%
# 슬라이스에 할당하기
"""
할당문의 왼쪽에 슬라이스 표기법을 사용하거나 
del 문의 대상 객체로 지정함으로써 
가변 시퀀스를 연결하거나, 잘라내거나, 값을 변경할 수 있다.
"""

myl = list(range(10))
print(myl)

myl[2:5] = [20, 30, 40]
print(myl)

myl[2:5] = [22, 33]
print(myl)

del myl[2:5]
print(myl)

myl = list(range(10))
print(myl)
myl[6::2] = [11, 22]
#myl[4::2] = [11, 22]  # error
#myl[4::3] = [11, 22]  # ok
#myl[4::2] = [11, 22, 33]  # ok
print(myl)

myl = list(range(10))
print(myl)
myl[2:5] = [100]
#myl[2:5] = 100  # TypeError: can only assign an iterable
print(myl)

#%%




