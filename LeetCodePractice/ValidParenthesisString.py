#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:23:38 2018

@author: owner
"""

def checkValidString(s):
    lo = hi = 0
    for char in s:
        lo += 1 if char == "(" else -1
        hi += 1 if char != ")" else -1
        if hi < 0:
            break
        lo = max(lo, 0)
    return lo == 0