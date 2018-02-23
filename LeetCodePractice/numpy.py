# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:47:19 2018

@author: donny
"""

import collections

import copy

s = 'I am a test sentence and I am very cute.'

s_list = s.split()

for item in s_list:
    if item.strip() not in ',.!"':
        if item not in s_dict:
            s_dict[item] = 1
        else:
            s_dict[item] += 1
print(s_dict)