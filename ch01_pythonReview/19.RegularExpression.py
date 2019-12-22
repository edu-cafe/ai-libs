# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:40:43 2019

@author: shkim
"""

# 정규식 이해-1
import re

text = 'some#+ 123 string~ SOME@STRING!!'
REGEX = re.compile('[a-z]')
#REGEX = re.compile('[a-z ]')
#REGEX = re.compile('[a-z0-9]')
#REGEX = re.compile('[a-zA-Z0-9]')
#REGEX = re.compile('[\w]')  # alpha-numeric
#REGEX = re.compile('\w')  # alpha-numeric
#REGEX = re.compile('[\w+]')  # alpha-numeric or '+'
#REGEX = re.compile('\w+')  # alpha-numeric iter --> string
#REGEX = re.compile('\W')  # not alphanumeric
#REGEX = re.compile('\s')  # white space
#REGEX = re.compile('\S')  # not white space
#REGEX = re.compile('\d')  # digits
#REGEX = re.compile('\D')  # not digits
#REGEX = re.compile('[\w\s]')  # alpha-numeric or white space
#REGEX = re.compile('\w\s')  # alpha-numeric and white space
result = REGEX.findall(text)
print(result)

#%%
# 정규식 이해-2
import re

text = '!@#abcde00 hello'
REGEX = re.compile('\w+')  # alpha-numeric iter --> string

result = REGEX.search(text) # search는 문자열 처음이 패턴과 맞지 않더라도 이후에도 맞는게 있는지 찾음.
print('--search--')
if result:
    print('group: ', result.group())
    print('start: ', result.start())
    print('end: ', result.end())
    print('span: ', result.span())
else:
    print("No match") 
    
#%%
# 정규식 이해-3
import re

text = '!@#abcde00 hello'
REGEX = re.compile('\w+')  # alpha-numeric iter --> string

result = REGEX.match(text) # match는 전체 문자열에서 처음부터 바로 패턴이랑 일치하는지 찾음. 없는 경우 None을 리턴
print('--match--')
if result:
    print('group: ', result.group())
    print('start: ', result.start())
    print('end: ', result.end())
    print('span: ', result.span())
else:
    print("No match")

#%%
# 정규식 이해-4
import re

text = '!@#abcde00 hello'
REGEX = re.compile('\w+')  # alpha-numeric iter --> string

find_result = REGEX.findall(text)
print('--findall--')
print(find_result)

#%%
# 정규식 이해-5
import re

text = '!@#abcde00 hello'
REGEX = re.compile('\w+')

iter_result = REGEX.finditer(text)
print('--finditer--')
if iter_result:
    for mo in iter_result:
        print('group: ', mo.group())
        print('start: ', mo.start())
        print('end: ', mo.end())
        print('span: ', mo.span())   

#%%
# 정규식 이해-6
import re
text = 'abc adc c abcc a ac acc aaac aaaac aaaaaac cb cc a0c aa00c a%c a1@#$c'
# REGEX = re.compile('a.c')
# REGEX = re.compile('a?c')
# REGEX = re.compile('a+c')
REGEX = re.compile('a*c')
result = REGEX.search(text)   # search는 문자열 처음이 패턴과 맞지 않더라도 이후에도 맞는게 있는지 찾음. 리턴?
# result = REGEX.match(text)   # match는 전체 문자열에서 처음부터 바로 패턴이랑 일치하는지 찾음. 없는 경우 None을 리턴
print(result)
print(result.start())

#%%
# 정규식 이해-7
import re
text = 'abc adc c abcc a ac acc aaac aaaac aaaaaac cb cc a0c aa00c a%c a1@#$c'
REGEX = re.compile('a.c')  # 1
#REGEX = re.compile('a?c')  # 0 or 1
#REGEX = re.compile('a+c')   # >=1 
#REGEX = re.compile('a*c') # >=0

iter_result = REGEX.finditer(text)
print('--finditer--')
if iter_result:
    for mo in iter_result:
        print('group: ', mo.group())
#         print('start: ', mo.start())
#         print('end: ', mo.end())
#         print('span: ', mo.span())   

#%%
# 정규식 이해-8
# dict.get()을 이용해서 인덱스에서 발생한 단어 목록을 가져와 갱신
""" 단어가 나타나는 위치를 가리키는 인덱스를 만든다 """
import re

WORD_RE = re.compile(r'\w+') # 찾고자 하는 패턴을 등록. w는 [a-zA-Z0-9]와 동일, +는 반복될 수 있음을 의미
index = {}

# encoding
# linux : utf-8, windows : cp949
# with open('README.md', encoding='utf-8') as fp:
with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1): # iterator start index is 1
        for match in WORD_RE.finditer(line):
            # match object는 다음 코드에서와 같이 group(), start(), end(), span() 네 가지 메소드를 가지고 있다.
            # group은 매치된 첫 번째 문자열을 리턴하고, start는 전체 텍스트에서 그 매치된 문자열의 시작 인덱스,
            # end는 매치된 문자열의 마지막 인덱스+1을 리턴한다. span은 시작, 끝 인덱스를 튜플로 리턴한다.            
            word = match.group().upper()
            column_no = match.start() + 1
            location = (line_no, column_no)
#            print('-->', word, column_no, location)
            """
            Following is the syntax for dict.get() method
            dict.get(key, default = None)
                <Parameters>
                key − This is the Key to be searched in the dictionary.
                default − This is the Value to be returned in case key does not exist.
            """
            occurrences = index.get(word, []) # 없으면 빈 리스트를, 있으면 dict에 저장된 기존 리스트를 가져옴
            occurrences.append(location)
            index[word] = occurrences # 줄번호와 단어의 시점번호의 조합인 튜플을, 해당 단어를 키로 사용하는 딕셔너리 항목에 추가함
#            index.setdefault(word, []).append(location) # 위의 3줄을 한줄로 바꿀 수 있다.
#            print('--> word:', word, 'index:',  index)

# 알파벳순으로 출력한다.
for word in sorted(index, key=str.upper):
    print(word, index[word])

#%%
# 정규식 이해-9
import re
import collections

WORD_RE = re.compile(r'\w+') # 찾고자 하는 패턴을 등록. w는 [a-zA-Z0-9]와 동일, +는 반복될 수 있음을 의미
index = collections.defaultdict(list) # 키가 없을 때 호출할 함수를 기본값으로 설정해 줌

with open('zen.txt', encoding='utf-8') as fp:
# with open('README.md', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1): # iterator start index is 1
        for match in WORD_RE.finditer(line):
            word = match.group().upper()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location) # 키 값이 없더라도 기본값인 list를 호출하여 빈 list를 대입한다.

# 알파벳순으로 출력한다.
for word in sorted(index, key=str.upper):
    print(word, index[word])

#%%


