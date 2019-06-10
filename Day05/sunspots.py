# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:41:20 2019

@author: kmh02
"""
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

months,number= np.loadtxt("sunspots.tsv",unpack = True) 
plt.plot(months,number)
plt.xlabel('Month')
plt.ylabel('Number of Spots')
plt.show()


N=3143
window_lst= [5]
avg=np.zeros((len(window_lst),N))
for i, window in enumerate(window_lst):
    avg2=np.ones(window)/window
    avg[i, :] = np.convolve(number,avg2, 'same')

plt.plot(months,avg[i,:] + (i+1)*50, label=window)
plt.xlabel("Months")
plt.ylabel("Average")
plt.show()