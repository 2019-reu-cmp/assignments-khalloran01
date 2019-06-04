# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:45:55 2019

@author: kmh02
"""
"""
1) for loop uses a variable, and a while loop has a given
condition that must be followed

2) It took one iteration to accurately calculate 6 decimal places.
It took two iterations to accurately calculate to the 12th decimal place. 
It took three iterations to become completely accurate for any further decimal points 

3) Two ways to access a file name: 
        f=open(filename, 'r')
        f.read()
        f.close()
    OR 
        with open(filename, 'r') as f: 
        wholefile = f.read()
        
        data = []
        for line in f:
            data. append(line)
Using one or the other depends on the size of the file
4) The "with" method is better to use because you don't have to enclose the file  
    
5) iterable: list, tuple, string, or generator; it returns data one object at a time 
    