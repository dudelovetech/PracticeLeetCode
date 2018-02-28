#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:23:38 2018

@author: owner
"""

def checkValidString(s):
    left = 0
    right = len(s) - 1
    if len(s) == 0 :
        return True
    else:
        while left < right:
            if s[left] != "(" and s[left] != "*":
                return False
            if s[right] != ")" and s[right] != "*":
                return False
            else:
                left += 1
                right -= 1
    return True

checkValidString("C")