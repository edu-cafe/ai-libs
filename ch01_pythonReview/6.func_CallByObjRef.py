# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:52:25 2019

@author: shkim
"""

def spam(eggs):
    print('\naddr_eggs1:', eggs.__add__)
    print('spam_eggs1:', eggs)
    eggs.append(1)      # 기존 객체의 주솟값에 1[] 추가
    eggs = [2, 3]       # 새로운 객체 생성
    print('\naddr_eggs2:', eggs.__add__)
    print('spam_eggs2:', eggs)


ham = [0]
print('-->main_addr_ham:', ham.__add__)
spam(ham)
print('\nmain_ham:', ham)
