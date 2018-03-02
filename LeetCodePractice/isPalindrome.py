#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:45:36 2018

@author: owner
"""

def isPalindrome(x):
    y = x
    new = 0
    if x.bit_length() > 31 | x < 0:
        return False
    while y != 0:
        remainder = y % 10
        new = new * 10 + remainder
        y = int(y/10)
    return x == new