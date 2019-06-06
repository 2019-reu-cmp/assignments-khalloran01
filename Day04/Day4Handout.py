# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:55:50 2019

@author: kmh02

'''
1. Strings and lists both store information; a user can access specific parts of each given certain methods
They differ because strings only hold letters where lists can hold both numbers and letters

2. List comprehensions process the information in the list faster, and is a better method than .append()

3. use try/except statement to check for matplotlib and then return version
"""
try:
    import matplotlib as mpl
except Exception as e:
    print ("matplotlib is not installed", e)
else:
    print('matplotlib version:', mpl.__version__)

"""
4.Function that performs dot product using enumerate, zip
"""

import math 

a=[1,2]
b=[3,4]

dotproduct = 0
for i, x in enumerate (a):
    dotproduct += b[i]*x
print (dotproduct)



dotproduct=0
for i,x in zip(a,b):
   dotproduct += i*x
print ("Dot product is:", dotproduct)
    