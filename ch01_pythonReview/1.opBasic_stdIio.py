# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:01:00 2019

@author: shkim
"""

# 정수형의 Max 값은??
a = 12345678901234567890
a
#%%
# 실수형의 Max 값은??
b = 1.2345678901234567890
b
#%%
a+b

#%%
print('abc', 'def')
print('abc' + 'def')

#%%
myInt = 123
myStr = '456'
print(myInt + int(myStr))
print(str(myInt) + myStr)
#print(myInt + myStr)    # error
#print(myStr + myInt)    # error

#%%
print("Enter your name:")
somebody = input()       # 콘솔 창에서 입력한 값을 somebody에 저장
print("Hi", somebody, "How are you today?")

#%%
name = input('Name? ')
print('\nName->', name)
#%%
print('%s, Welcome!!', name)
print('%s, Welcome!!' % name)

#%%
age = int(input("Age? "))
print('Name:%s, Age:%d' % (name, age))
#%%
print('Name:{}, Age:{}'.format(name, age))
print('Name:{0}, Age:{1}'.format(name, age))
print('Age:{1}, Name:{0}'.format(name, age))


