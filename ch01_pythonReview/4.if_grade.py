# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:58:39 2019

@author: shkim
"""

score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'

print(grade)

#%%
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)

#%%
score = int(input("Enter your score: "))

if ( 90 <= score ):
    grade = 'A'
if ( 80 <= score < 90 ):
    grade = 'B'
if ( 70 <= score < 80 ):
    grade = 'C'
if ( 60 <= score < 70 ):
    grade = 'D'
if ( score < 60 ):
    grade = 'F'

print(grade)



