# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:04:37 2017

@author: donny
"""

while True:
    try:
        count = int(raw_input("Enter count: "))
        price = int(raw_input("Enter price for each one: "))
        total_price = count * price
        print "Pay:" , total_price
        break
    except ValueError:
        print("Error, please enter numeric one.")
