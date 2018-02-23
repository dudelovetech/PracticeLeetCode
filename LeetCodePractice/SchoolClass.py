# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 22:43:20 2018

@author: donny
"""

class roster(object):
    "students and teacher class"
    teacher = ""
    students = [ ]

    def __init__(self,tn='mayun'):
        self.teacher = tn

    def add(self, sn):
        self.students.append(sn)

    def remove(self, sn):
        self.students.remove(sn)

    def print_all(self):
        print("Teacher:", self.teacher)
        print("Students:", self.students)