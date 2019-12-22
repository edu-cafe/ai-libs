# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:22:34 2019

@author: shkim
"""

"""
# 키워드 인수 (keyward arguments)
"""
#%%
def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("kim", "lee")
print_something("lee", "kim")
print_something(your_name = "lee", my_name = "kim")

#%%
def kwargs_test( **kwargs ):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs['first'])
    print(*kwargs)
    print("{second}".format(**kwargs))
    print("First value is {first}".format( **kwargs ))
    print("Second value is {second}".format( **kwargs ))
    print("Third value is {third}".format( **kwargs ))

kwargs_test(first = 3, second = 4, third = 5)
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error

#%%
def kwargs_test(*kwargs):
    print(kwargs)
    print("First value is {}".format(*kwargs))
    print("Second value is {}".format(*kwargs))
    print("Third value is {}".format(*kwargs))

kwargs_test(3, 4, 5)  # ok

#%%
args = {'first':3, 'second':4, 'third':5}
print('second:{second}'.format(**args))

#%%
args = {3, 4, 5}
print('value:{1}'.format(*args))

#%%
"""
# 디폴트 인수 (default arguments)
"""
#%%
def print_something(my_name, your_name='park'):
    print("Hello {}, My name is {}".format(your_name, my_name))

print_something("kim", "lee")
print_something("kim")
print_something(my_name = "kim")

#%%
# error
def print_something(my_name='lee', your_name):
    print("Hello {}, My name is {}".format(your_name, my_name))
    
#%%
def print_something(my_name='lee', your_name='park'):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("kim", "lee")   
print_something("kim")
print_something()

#%%
"""
# 가변 인수 (variable arguments)
"""
#%%
def vararg_test(a, b, *args):
    print(args)

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5

#%%
def vararg_test(a, b, *args):
    [*c] = args
    d = args
    print(args.__add__, c.__add__, d.__add__)
    print(args, c, d)
#    args[1] = 44  # error
#    d[1] = 44  # error
#    c[1] = 44  # ok

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


#%%
# ok in python3.6
# error in python3.7
def vararg_test(a, b, *args):
    return a + b + sum(args)

print(vararg_test(1, 2, 3, 4, 5))  # 15

#%%
# ok in python3.6
# error in python3.7
a = [1,2,3,4,5]
sum(a)


