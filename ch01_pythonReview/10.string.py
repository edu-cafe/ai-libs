# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:28:39 2019

@author: shkim
"""

"""
# 문자열 서식 지정
"""
#%%
print(1, 2, 3)
print("%d %d %d" % (1, 2, 3))
print("a" + " " + "b" + " " + "c")
print("{} {} {}".format(1, 2, 3))

#%%
print('%s %s' % ('one', 'two'))
print('%c %c' % ('a', 'b'))
print('%s %s' % ('a', 'b'))
print("{} {} {}".format("a", "b", "c"))

#%%
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
day = "three"
print("I ate %d apples. I was sick for %s days." % (number, day))

#%%
"""
# 문자열의 연산 
"""
#%%
str = "My name is Kim SooHyun"
str.upper()

#%%
str

#%%
str.lower()

#%%
str.title()

#%%
str.capitalize()

#%%
str.count('m'), str.count('M')

#%%
str.isdigit(), str.startswith('m'), str.startswith('M')

#%%
text = 'Good morning, Kim!!'.lower().split()
text

#%%
text = 'Good morning, Kim!!'.lower().split(',')
text

#%%
colors = ['red', 'blue', 'green', 'gray']
rst = ''.join(colors)
rst
