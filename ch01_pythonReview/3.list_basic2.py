# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:33:23 2019

@author: shkim
"""

k_s = [10, 20, 30, 40]
m_s = [11, 22, 33, 44]
e_s = [50, 60, 70, 80]

midterm_s = [k_s, m_s, e_s]
midterm_s

#%%
midterm_s[1][3]

#%%
midterm_s[1]

#%%
m_s[1] = 100
midterm_s

#%%
a = 300
b = 300

print(a is b)  # address
print(a == b)  # value

#%%
# -5부터 256까지의 정수값을 특정 메모리 주소에 저장함
a = 1
b = 1

print(a is b)  # address
print(a == b)  # value

#%%
a = [9, 2, 7, 4, 6]
b = [11, 22, 33, 44, 55, 66]

b = a
b

#%%
a.sort()
b
