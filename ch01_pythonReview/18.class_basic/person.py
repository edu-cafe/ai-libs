# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:12:55 2019

@author: shkim
"""

class Person(object):                       # 부모 클래스 Person 선언
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):                     # 메서드 선언
        print("저의 이름은", self.name, "이고요, 제 나이는", str(self.age), "살입니다.")
        
