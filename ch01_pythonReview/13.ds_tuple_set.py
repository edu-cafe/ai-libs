# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:37:58 2019

@author: shkim
"""

"""
# Tuple
"""
#%%
t = (1, 2, 3, 4, 5)

t[0], t[:], t[:3], t[3:], t[-1]

#%%
t+t, t*2

#%%
"""
튜플과 리스트는 거의 유사하지만, 튜플의 값은 마음대로 변경할 수 없다는 것임
만약 튜플의 값을 변경하고 싶다면 다음과 같이 오류가 발생함
"""
# error
t[1] = 22

#%%
"""
# Set
"""
#%%
s = set()
type(s), s

#%%
s = {1, 2, 3, 2}
type(s), s

#%%
s = set([1, 2, 3, 2, 4, 5, 3])
type(s), s

#%%
s = {1, 2, 3}
s.add(4)
s

#%%
s.remove(2)
s

#%%
s = {1, 2, 3}
s.update([4, 7, 3, 6, 1])
s

#%%
s.discard(3)
s

#%%
s.clear()
s

#%%
# 주의 : dictionary 임 
s = {}
type(s), s  # (dict, {})

#%%
s1 = {1, 2, 3, 4, 5}
s2 = set([3, 4, 5, 6, 7])

s1.union(s2)  # {1. 2. 3. 4. 5. 6. 7}

#%%
s1 | s2  # {1, 2, 3, 4, 5, 6, 7}

# s1 + s2    # error
#%%
s1.intersection(s2)  # {3, 4, 5}

#%%
s1 & s2  # {3, 4, 5}

#%%
s1.difference(s2)  # {1, 2}

#%%
s1 - s2  # {1, 2}








