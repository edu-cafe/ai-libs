# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:28:38 2019

@author: shkim
"""

print('Start mainTest1..')

def func():
    print('mainTest1_func()..')   

def addition(x, y):
    return x + y

def multiplication(x, y):
    return x * y

print(addition(10, 5))
print(multiplication(10, 5))
    
#if __name__ == '__main__':
#    print('-->mainTest1 runs as main..')
#    print(addition(10, 5))
#    print(multiplication(10, 5))
#else:
#    print('mainTest1 is imported..')