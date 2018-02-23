# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 20:46:09 2018

@author: donny
"""

# -*- coding: utf-8 -*-
"""
string count

@author: Dazhuang
"""
def countchar(s):
    lst = [0] * 26
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <='z':  
            lst[ord(s[i])- ord('a')] += 1
    print(lst)

if __name__ == "__main__":
    s = "Hope is a good thing."
    s = s.lower()
    countchar(s)