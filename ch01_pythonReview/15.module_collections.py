# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:38 2019

@author: shkim
"""

"""
# deque
"""
#%%
# Stack

from collections import deque
dq_list = deque()
for i in range(5):
    dq_list.append(i)

dq_list

#%%
dq_list.pop(), dq_list.pop(), dq_list

#%%
# Queue

from collections import deque
dq_list = deque()
for i in range(5):
    dq_list.appendleft(i)

dq_list

#%%
dq_list.pop(), dq_list.pop(), dq_list

#%%
# Circular Queue - rotate()

from collections import deque
dq_list = deque()
for i in range(5):
#    dq_list.appendleft(i)
    dq_list.append(i)

dq_list

#%%
dq_list.rotate(2)
dq_list

#%%
dq_list.rotate(2)
dq_list

#%%
# reverse()

from collections import deque
dq_list = deque()
for i in range(5):
    dq_list.append(i)

dq_list

#%%
dq_list.reverse()
dq_list

#%%
# extend(), extendleft()

dq_list = deque([0, 1, 2, 3, 4])
dq_list.extend([5, 6, 7])
dq_list

#%%
dq_list = deque([0, 1, 2, 3, 4])
dq_list.extendleft([5, 6, 7])
dq_list

#%%
"""
# Ordering Dictionary
"""
#%%
d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

#%%
from collections import OrderedDict         

d = OrderedDict()

d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

for k, v in d.items():
    print(k, v)

#%%
from collections import OrderedDict   

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

def sort_by_key(t):
    return t[0]      

od = OrderedDict(sorted(d.items(), key=sort_by_key))
od.items()

#%%
from collections import OrderedDict   

d = {}
d['x'] = 100
d['l'] = 500
d['y'] = 200
d['z'] = 300

def sort_by_value(t):
#    print(t[0], t[1])
    return t[0] 
#    return t[1]     

#%%
d.items()
#%%
sorted(d.items(), key=sort_by_value)   
#%%
od = OrderedDict(sorted(d.items(), key=sort_by_value))
od.items()

  
#%%
"""
# Default Dictionary
"""
#%%
d = dict()
print(d["first"]) # key error 

#%%
from collections import defaultdict

d = defaultdict(lambda: 0)          # Default 값을 0으로 설정
print(d["first"], d['bb'])
d.items()

#%%
# error : yellow key
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = dict()
for k, v in s:
    d[k].append(v)

print(d.items())

#%%
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items()) # [('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])]


#%%
# collections 응용-1 : text 내에 포함된 각 단어의 수를 출력하라

# split() : space로 분리, split(',')
text = """A press release is the quickest and easiest way to get free \
  publicity. If well written, a press release can result in multiple \
  published articles about your firm and its products. And that can mean \
  new prospects contacting you asking you to sell to them. ….""".lower().split()
type(text), text[:10]

#%%
from collections import defaultdict

word_count = defaultdict(lambda: 0)             # Default 값을 0으로 설정
for word in text:
    word_count[word] += 1
word_count

#%%
from collections import OrderedDict
od = OrderedDict(sorted(word_count.items(), key=lambda t: t[0])).items()
od

#%%
od = OrderedDict(sorted(word_count.items(), key=lambda t: t[1])).items()
od

#%%
od = OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items()
od

#%%
from collections import OrderedDict
#for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1])).items():
    print(i, v)

#%%
"""
# Counter Module
"""
#%%
from collections import Counter

text = list('Good morning everybody!!')
type(text), text[:10]

#%%
c =Counter(text)
print(c)
c['o'], c['e'], c['g']

#%%
c =Counter(['banana', 'pear', 'apple', 'apple', 'banana', 'grape'])
print(c)
c['banana'], c['pear'], c['apple']


#%%
# collections 응용-1 : text 내에 포함된 각 단어의 수를 출력하라

text = """A press release is the quickest and easiest way to get free \
  publicity. If well written, a press release can result in multiple \
  published articles about your firm and its products. And that can mean \
  new prospects contacting you asking you to sell to them. ….""".lower().split()
type(text), text[:10]

#%%
from collections import Counter

c = Counter(text)
c


#%%
from collections import Counter

c = Counter({'red':3, 'blue':1, 'gray':4})
print(c)
print(c.values())
print(list(c.values()))

#%%
list(c.keys())

#%%
list(c.elements())

#%%
from collections import Counter

c = Counter(cats=3, dogs=5)
list(c.elements())

#%%
# 덧셈, 뺄셈, 논리연산  

from collections import Counter

c1 = Counter(a=3, b=5, c=2)
c2 = Counter(a=-1, b=3, c=7)
c1.subtract(c2)  #뺄셈
print(c1)
print(list(c1.elements()))

#%%
from collections import Counter

c1 = Counter(a=3, b=5, c=2)
c2 = Counter(a=-1, b=3, c=7)
c1 + c2  # 덧셈
#%%
c1 & c2  # 논리 AND
#%%
c1 | c2  # 논리 OR

#%%
"""
# namedtuple Module
"""
#%%
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(type(p), p)
print(p.y, p[1])

#%%
p = Point(11, y=22)
p

#%%
p = Point(y=11, x=22)
p, p.x, p.y, p[0], p[1]

#%%