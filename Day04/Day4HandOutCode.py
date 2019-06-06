# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:59:01 2019

@author: kmh02
"""


try:
    import matplotlib as mpl
except Exception as e:
    print ("matplotlib is not installed", e)
else:
    print('matplotlib version:', mpl.__version__)