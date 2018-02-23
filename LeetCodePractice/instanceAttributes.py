# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 22:13:44 2018

@author: donny
"""

class Dog(object):
    "define Dog class"

    counter = 0
    
    def __init__(self,name):
        self.name = name        
        Dog.counter += 1
        
    def greet(self):
        print("woof woof woof, my name is %s." %self.name)
        Dog.counter
        
if __name__ == '_main_':
    dog = Dog("Sugar")
    dog.greet()
            
Juice = Dog("Juice")
Juice.greet()

Peter = Dog("Peter")
Peter.greet()