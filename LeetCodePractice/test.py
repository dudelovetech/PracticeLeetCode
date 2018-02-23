# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:48:53 2018

@author: donny
"""

def find_person(dict_users, strU):
      if dict_users.has_key(strU):
          return dict_users[strU]
      else:
          return 'Not Found'

if __name__ == "__main__":
     dict_users = {'Tom':88888,'Jerry':5555555,'Snoopy':11111,'Pooh':12341234,'Luffy':1212121}
     strU =  input('Please input the name: ')
     print(find_person(dict_users, strU))