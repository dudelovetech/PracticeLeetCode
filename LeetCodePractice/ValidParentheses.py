#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:55:48 2018

@author: owner
"""

def isValid(s):

    dic = {'(':')', '[':']', '{':'}'}
    q = []
    
    for char in s:
        if char in dic:
            q.append(char)
        else:
            if not q or char != dic[q.pop()]:
                return False
    return True if not q else False