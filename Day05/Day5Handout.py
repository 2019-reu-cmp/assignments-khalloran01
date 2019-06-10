# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:26:47 2019

@author: kmh02
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplotlib
"""
1) Why np.array() instead of a list for numbered list? 
Numpy performs functions better, and are faster than lists.
Numpy also has specific functions that a normal list does not, such as linear
algebra operations. Numpy takes up less memory space as well. 

2)Explore basic math functions: 
"""


a= np.array([0,1,2])
b= np.arange(3)
c=np.linspace(0,2,3)

print (a+b)
print (a.mean())
print (a*b)

"""
Array math functions apply to each spot in the array individually. 
Instead of adding all the values together (like 0+1+2), it adds each value
in each spot together (0+0, 1+1, 2+2)

3) Statistical functions with multi-d arrays? 
"""
print (a.mean(axis=0)): "This applies whatever function is being called to the specified line
"""For example, in a 2D array, axis = 1 would mean the second line, meaning it would find the mean of the second line 
4)Histogram of values from sunspots.
"""
months, number= np.loadtxt("sunspots.tsv",unpack = True) 
plt.hist(number, bins = 50)
plt.xlabel("number of spots in month")
plt.ylabel("months with this many spots")
plt.title("Sunspot Number Distribution")
plt.show()