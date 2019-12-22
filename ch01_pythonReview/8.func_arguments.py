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
print_something( ............ )

#%%
def kwargs_test( ...... ):
    print(kwargs)
    print("First value is {first}".format( .... ))
    print("Second value is {second}".format( .... ))
    print("Third value is {third}".format( .... ))

kwargs_test(first = 3, second = 4, third = 5)
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error


#%%
"""
# 디폴트 인수 (default arguments)
"""
#%%
def print_something(my_name, your_name='park'):
    print("Hello {}, My name is {}".format(your_name, my_name))

print_something("kim", "lee")
.....




#%%
"""
# 가변 인수 (variable arguments)
"""
#%%
def vararg_test(a, b, .... ):
    print(args)

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


#%%
def vararg_test(a, b, .... ):
    .... = args
    print(args, c, d)
	c[1] = 44

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


