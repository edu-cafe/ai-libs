# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:43:44 2019

@author: shkim
"""
#%%
"""
Sequence
- Container sequences : list, tuple, and collections.deque
- Flat sequences : str, bytes, bytearray, memoryview, and array.array
Sequence
- Mutable sequences : list, bytearray, array.array, collections.deque, and memoryview
- Immutable sequences : tuple, str, and bytes
"""

#%%
"""
# List Comprehensions, 지능형 리스트 
"""
#%%
# list + for
rst = []
for i in range(10):
    rst.append(i)
rst

#%%
# list comprehensions
rst = [i for i in range(10)]
rst

#%%
# list + for
rst = []
for i in range(10):
    if i % 2 == 0: rst.append(i)
rst

#%%
# list comprehensions : filtering
rst = [i for i in range(10) if i%2 == 0]
rst

#%%
# list comprehensions : filtering
rst = [i if i%2 == 0 else 10 for i in range(10)]
rst

#%%
# list comprehensions : nested for
s1 = 'abc'
s2 = '12'
rst = [i+j for i in s1 for j in s2]
rst

#%%
# list comprehensions : nested for && filtering
s1 = 'abc'
s2 = '12'
s3 = 'cda'
rst = [i+j for i in s1 for j in s2 if (i!=j)]
rst

#%%
rst = [i+j for i in s1 for j in s3 if (i==j)]
rst

#%%
# list comprehensions : 2d list
words = 'The quick brown fox jumps over the lazy dog'.split()
#words
rst = [[len(w), w.upper(), w.lower()] for w in words ]
rst

#%%
# list comprehensions : 2d list
s1 = 'abc'
s2 = '12'
rst = [[i+j for i in s1] for j in s2]
rst

#%%
#%%
#%%
symbols = '$#$%*&'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)    


symbols = '$#$%*&'
codes = [ord(symbol) for symbol in symbols]
print(codes) 

#%%
# 변수가 더 이상 누락되지 않는 Listcomps, Listcomps No Longer Leak Their Variables
x = 'hello,kim'
dummy = [x for x in 'ABC']
print(dummy)
print(x)

x = 'hello,kim'
dummy = [ord(x) for x in x]
print(dummy)
print(x)

#%%
import collections
lst = []
print(isinstance(lst, collections.abc.Sequence)) # collections.abc.Sequence에 포함됨
print(type(lst))

print(isinstance(lst, collections.abc.MutableSequence)) # collections.abc.MutableSequence에 포함됨
print(type(lst))

#%%
# Listcomps vs. map and filter
symbols = '$#$%*&(+'
codes = [ord(symbol) for symbol in symbols]
print(codes)

codes = [ord(symbol) for symbol in symbols if ord(symbol) < 40]
print(codes)

codes = list(filter(lambda c: c < 40, map(ord, symbols)))
print(codes)


#%%
# Cartesian product using a list comprehension
"""
[ ], { }, ( ) 안에서의 개행은 무시된다. 
따라서 줄을 넘기기 위해 역슬래시()를 사용하지 않고도 여러줄에 걸쳐 리스트, 지능형 리스트, 제너레이터 표현식, 딕셔너리를 작성할 수 있다.
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
#tshirts = [(color, size) for color in colors for size in sizes]
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

print('---------------')
for color in colors:
    for size in sizes:
        print((color, size))
#%%
# Cartesian product using a list comprehension
ranks = ['A', 'K', 'Q']
suits = ['spades', 'hearts', 'diamonds', 'clubs']
cp = [(rank, suit) for rank in ranks for suit in suits]
print(cp)

#%%
