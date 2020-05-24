# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:46:40 2020

@author: USMM005
"""


import pandas as pd
import matplotlib.pyplot as plt

# read the data from the working directory
df = pd.read_csv('zomato.csv')

#number of rows and columns
df.shape

# returns the first 10 number of rows and columns
df.head(10)

#returns the last n number of rows and columns
df.tail()

#returns all the column headers
df.columns

#returns the  basic information of all the columns
df.info()

#returns the basic statistics on the numeric columns
df.describe()

#returns the data types 
df.dtypes

#displays all the values which is null
df.isnull()

#displays the columns that has null values
df.isnull().any()


######### graphs##########

states = ['chicago','newyork','california','portland','ohio']

pop = [3.5,6.7,8.9,3.4,6.5]

figure = plt.figure(figsize = (8,6))
plt.plot(states)
plt.show()

plt.title("population graph")
