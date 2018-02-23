# -*- coding: utf-8 -*-
"""
Created on Mon Jan 01 22:30:59 2018

@author: donny
"""

aStr = "Hello, World!"
bStr = aStr[:7] + "Python!"
count = 0
for ch in bStr[:]:
    if ch in ',.!?':
        count += 1
print('There are {0:d} punctuation marks.'.format(count))