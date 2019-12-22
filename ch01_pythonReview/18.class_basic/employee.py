# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:13:36 2019

@author: shkim
"""

from person import Person

class Employee(Person):                                             # 부모 클래스 Person으로부터 상속
#    def __init__(self, name, age, gender, salary, hire_date):
#        super().__init__(name, age, gender)                         # 부모 객체 사용
#        self.salary = salary
#        self.hire_date = hire_date                                  # 속성값 추가
        
    def __init__(self, person, salary, hire_date):
#        self.person = person
        super().__init__(person.name, person.age, person.gender)                         # 부모 객체 사용
        self.salary = salary
        self.hire_date = hire_date                                  # 속성값 추가

    def do_work(self):                                              # 새로운 메서드 추가
        print(self.name + "-->열심히 일을 한다.")

    def about_me(self):                                             # 부모 클래스 함수 재정의
        super().about_me()                                          # 부모 클래스 함수 사용
        print("제 급여는", self.salary, "원이고, 제 입사일은", self.hire_date, "입니다.")

