# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:43:44 2019

@author: shkim
"""
#%%
symbols = '$#$%*&'
codes = [ord(symbol) for symbol in symbols]
print(codes) 
print(type(codes))
#codes.append(10)    # ok

symbols = '$#$%*&'
codes = tuple(ord(symbol) for symbol in symbols)
print(codes) 
print(type(codes))
#codes.append(10)    # error

#%%
import array
symbols = '$#$%*&'
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)
print(type(a))
a.append(10)
print(a)

#%%
# Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
t_gen = ( (color, size) for color in colors for size in sizes )
print(t_gen)
print(type(t_gen))
tshirts = list(t_gen)
print(tshirts)
print(type(tshirts))

print('----------------')
for tshirt in ((c, s) for c in colors for s in sizes):
    print(tshirt)
    
#%%
# generator example
range(10)

