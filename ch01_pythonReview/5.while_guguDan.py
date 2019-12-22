# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:48:40 2019

@author: shkim
"""

dan = 1
while(dan):
#    print("\n구구단 몇 단을 계산할까요(1~9, 0 to quit)?")
#    x = int(input())
    dan = input("\n구구단 몇 단을 계산할까요(1~9, 0 to quit)? ")
    dan = int(dan)
    if dan == 0: break
    if not(1 <= dan <= 9):
        print("잘못 입력했습니다", "1부터 9 사이 숫자를 입력하세요.")
        continue
    else:
        print("구구단 " + str(dan) + "단을 계산합니다.")
        for i in range(1,10):
            print(str(dan) + " x " + str(i) + " = " + str(dan*i))

print("구구단 게임을 종료합니다.")

