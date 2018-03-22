# -*- coding: utf-8 -*-
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Created on Sat Feb 24 22:02:53 2018

@author: donny
"""

import sys

# -*-
#   SYMBOL       VALUE
#   I             1
#   IV            4
#   V             5
#   IX            9
#   X             10
#   XL            40
#   L             50
#   XC            90
#   C             100
#   CD            400
#   D             500
#   CM            900 
#   M             1000 

def romanToInt(Roman):
    # create a dictionary to store the one-on-one relationship between Roman numerals and the value it represents in decimal
    convert_table = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    # convert string into a list of characters
    char_list = list(Roman)
    
    if len(char_list) == 0:
        return 0
    
    # create an array to save the converted values from Roman numerals
    arr = []
    # convert each symbol of Roman Numerals into the value it represents
    for char in char_list:
        if char in convert_table:
            arr.append(convert_table.get(char))
        else:
            sys.exit("there is a non-Roman letter")
        
    #result
    result = 0
    
    # Take symbol one by one from starting from index 0: 
    # If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
    # else subtract this value by adding the value of next symbol to the running total.
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            result += arr[i]
        else:
            result -= arr[i]
    # because there is no extra value for the last index value to compare with, we simply add it to the result        
    result += arr[len(arr)-1]       
    
    return result