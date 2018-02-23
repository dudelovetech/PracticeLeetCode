# -*- coding: utf-8 -*-
"""
Created on Sun Feb 04 21:16:14 2018

requirements: Calculate and output the standard deviation of males’ and females’ user scores in the data set “MovieLens 100k”.
relevant functions for possible use:
    
pandas.read_table(filepath_or_buffer, sep='\t', names=None)
pandas.pivot_table(data, values=None, columns=None, aggfunc='mean')
pandas.merge(left, right, how='inner')

@author: donny
"""

import pandas as pd
#from datetime import date

u_data = pd.read_table('C:\Users\donny\Downloads\ml-100k\ml-100k\u.data',header=None)
u_user = pd.read_table('C:\Users\donny\Downloads\ml-100k\ml-100k\u.user',sep='|',header=None)

cols = ['user id' , 'item id' , 'rating' , 'timestamp']
u_data.columns = cols

cols = ['user id' , 'age' , 'gender' , 'occupation' , 'zip code']
u_user.columns = cols

""" convert into normal time format """

#list1 = []
#
#for i in range(len(u_data)):
#    x = date.fromtimestamp(u_data.at[i,'timestamp'])
#    y = date.strftime(x,'%Y %m-%d')
#    list1.append(y)
#    
#u_data.loc[:,['timestamp']] = list1

ratings_mean = u_data.rating.mean()

full_table = u_data.merge(u_user, left_on = 'user id', right_on = 'user id',  how = 'inner')

female_rating = full_table.rating[full_table.gender=='F']
male_rating = full_table.rating[full_table.gender=='M']

print(female_rating.mean())
print(male_rating.std())