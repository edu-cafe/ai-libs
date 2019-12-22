# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:16:11 2019

@author: shkim
"""

from person import Person
from employee import Employee

if __name__ == '__main__':
    p1 = Person('kim', 25, 'f');    
    p2 = Person('park', 33, 'm');    
    p3 = Person('park', 32, 'f');
    
    p1.about_me()
    p2.about_me()
    p3.about_me()
    
    
    
#    e1 = Employee('kim', 25, 'f', 2400, '2018-01-05')
#    e2 = Employee('park', 33, 'm', 7400, '2015-11-15')
#    e3 = Employee('park', 32, 'f', 6500, '2017-08-05')
    e1 = Employee(p1, 2400, '2018-01-05')
    e2 = Employee(p2, 7400, '2015-11-15')
    e3 = Employee(p3, 6500, '2017-08-05')
    
    e1.about_me()
    e2.about_me()
    e3.about_me()
    
    e1.do_work()
    e3.do_work()
    