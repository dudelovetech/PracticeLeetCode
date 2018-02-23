# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:42:16 2017

@author: donny
"""

def proc(n):
    if n < 0:
        print('-', '')
        n = -n
    if n  // 10:
        proc(n  //  10 )
    print(n % 10,  '')

proc(-345 )