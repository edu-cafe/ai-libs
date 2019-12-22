# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:22:15 2019

@author: shkim
"""

colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[2])
print(len(colors))

#%%
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[0:6]

#%%
cities[0:20]

#%%
cities[:5]

#%%
cities[5:]

#%%
cities[:]

#%%
cities[-1:]

#%%
cities[-5:-1]

#%%
cities[-8:]

#%%
cities[-10:]

#%%
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']

len(color1), len(color2)

#%%
color3 = color1 + color2

color3

#%%
color1 * 2

#%%
'blue' in color1

#%%
color1.append('white')

color1

#%%
color1.append(color2)

color1

#%%
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']

color1.extend(color2)
color1

#%%
color1 = ['red', 'blue', 'green']

color1.insert(1, 'white')
color1

#%%
color1.remove('blue')
color1

#%%
color1 = ['red', 'blue', 'green']
color1[0] = 'white'
color1

#%%
del color1[0]
color1

#%%
# unpacking
t = [1, 2, 3]
a, b, c = t

a, b, c

#%%
# unpacking
t = [1, 2, 3]
a, b, c, d = t  # error

#%%
# packing
t2 = t, a, c

t2

#%%
