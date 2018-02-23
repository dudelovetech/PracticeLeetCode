# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 00:38:13 2018

@author: donny
"""

def fib(n):
    a, b = 0, 1
    count = 1
    while count  < n:
        a, b = b, a+b
        count = count + 1
    print(a)
    print(b)