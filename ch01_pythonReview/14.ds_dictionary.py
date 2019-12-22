# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:38 2019

@author: shkim
"""

d1 = dict()
d2 = {}

type(d1), d1, type(d2), d2

#%%
info = {1:'kim', 2:'park', 3:'lee'}
info

#%%
info[2]

#%%
info[5] = 'choi'
info

#%%
info[1] = 'whang'
info

#%%
info.keys()

#%%
info.values()

#%%
info.items()

#%%
for k, v in info.items():
    print('key:{}, value:{}'.format(k, v))

#%%
3 in info.keys(),  'lee' in info.values()

#%%