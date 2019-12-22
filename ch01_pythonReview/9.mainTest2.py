# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:32:30 2019

@author: shkim
"""

import mainTest1 as test1

print('Start mainTest2..')

test1.func()

if __name__ == '__main__':
    print('-->mainTest2 runs as main..')
else:
    print('mainTest2 is imported..')