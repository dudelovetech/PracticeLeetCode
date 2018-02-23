# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 01:04:50 2018

@author: donny
"""

with open('test.txt', 'rb', 0) as fp:
    fp.readline()
    fp.seek(10, 1)
    print(fp.readline())


#fruits = ['apple', 'banana', 'cherry','banana', 'peach', 'pear','peach', 'cherry' ]
#d = {}
#for item in fruits:
#	  d[item] = d.setdefault(item,0) + 1
#
#def compute(*numbers):    
#    sum = 1
#    for n in numbers:    
#        sum = sum * n + n    
#    return sum
#
##nums = (3,3)
##print(compute(*nums))
##print(compute([3,2,1]))
#nums = [1,2,3]
#print(compute(nums))