# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 00:41:16 2018

@author: donny
"""

def ask(prompt = "Do you like Python? ", hint = "yes or no"):
    while True:
        answer = input(prompt)
        if answer.lower() in ('y', 'yes'):
            print("Thank you")
            return True
        if answer.lower() in ('n', 'no'):
            print("Why not ")
            return False
        else:
            print(hint)