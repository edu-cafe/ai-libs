# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:45:33 2019

@author: shkim
"""
#%%
# Tuple used as records
lax_coordinates = (33.9425, -118.408056) #로스앤젤레스 국제공항 위/경도
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) #도쿄정보(지명,년도,인구수,인구변화율,면적)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')] #국가코드,여권번호
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# _ : dummy variable
for country, _ in traveler_ids:
    print(country)


#%%
# Parallel Assignment
lax_coordinates = (33.9425, -118.408056) #로스앤젤레스 국제공항 위/경도
latitude, logitude = lax_coordinates# Tuple Unpacking
print(latitude)
print(logitude)

#%%
# 튜플 언패킹을 이용하면 임시변수를 사용하지 않고 두 변수 값을 바꿀 수 있음
a=10
b=20
print('before:', a, b)
a, b = b, a
print('after:', a, b)

#%%
# 함수 호출 시 인자 앞에 *를 붙여서 튜플을 언패킹할 수 있음
print(divmod(20, 8))

t = (20, 8)
#t = [20, 8]  # ok
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)

#%%
# 파일시스템 경로에서 경로명과 파일명의 분리
import os
pathname, filename = os.path.split('/home/shkim/lab/test.py')
print(pathname)
print(filename)

_, filename = os.path.split('/home/shkim/lab/test.py')
print(filename)


# _ : gettext.gettext() 함수에 대한 별명

#%%
# 초과 항목을 잡는 *
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

#%%
# 내포된(Nested) 튜플의 언패킹
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

# ^ : 중간 정렬 
print('{:15} | {:^10} | {:^10} |'.format('', 'lat.', 'longi.'))
#print('{:15} | {:10} | {:10} |'.format('', 'lat.', 'longi.'))
#print('{2:15} | {1:^10} | {1:^10} |'.format('', 'lat.', 'longi.'))

fmt = '{:15} | {:10.4f} | {:10.4f} |'
#fmt = '{:15} | {:^10.4f} | {:^10.4f} |'
for name, cc, pop, (latitude, longitude) in metro_areas:
#for name, cc, pop, latitude, longitude in metro_areas:  # nok
#for name, cc, pop, [latitude, longitude] in metro_areas:  # ok
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

for name, cc, pop, coord in metro_areas:  # ok
    print(fmt.format(name, latitude, longitude))
 
#%%       
# Named Tuple
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
mycard = Card('3', 'spades')
print(mycard)

#%%
# Named Tuple
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
#City = namedtuple('City', 'name country population coordinates'.split())

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.country)
print(tokyo.coordinates)
print(tokyo[1])

#%%
#Named Tuple - Attributes, Methods
"""
_fields : 클래스의 필드명을 담고 있는 튜플
_make() : 반복형 객체로부터 몀명된 튜플을 만듬
_asdict() : 명명된 튜플 객체에서 만들어진 collections.OrderedDict 객체를 반환함
"""
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
print(City._fields)
print('------------------------------')
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
#delhi = City(*delhi_data)
delhi = City._make(delhi_data)
print(delhi)
print('------------------------------')
print(delhi._asdict())  # ordered dictionary로 바꿔줌 

#%%
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
for key, value in delhi._asdict().items():
    print(key + ':', value)
    
print('------------------------------')
cityList = list()
cityList.append(delhi)
cityList.append(delhi)
    
print(cityList[0].name)
print(cityList[0].population)
