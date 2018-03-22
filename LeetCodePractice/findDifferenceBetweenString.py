# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 22:21:11 2018

@author: donny
"""

S = 'how you doing'
T = 'how are you doing'

def findTheDiff (S, T):
    
    if not T:
        return []
    
    if len(S) < len(T):
        raise ValueError("T must be a substring of S")
    
    diff = []
    j = 0
    for i in range (0, len(S)):
        if T[j] != S[i]:
            diff.append(S[i])
            continue
        j += 1
    
    return diff    
        
        
print(findTheDiff(S, T))