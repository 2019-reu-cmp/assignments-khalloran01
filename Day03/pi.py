#!/usr/bin/env python3
""" pi.py - 
"""
import math

def srinivasa(k):
    i=0
    calc=0
    con=(2*(math.sqrt(2))/9801)
    while i<k:
        calc+=(math.factorial(4*i)*(1103+26390*i))/(((math.factorial(i))**4)*(396**(4*i)))
        print("i", i)
        i+=1 
    total= 1/(con*calc)
    return total, total-(math.pi)
    
if __name__ == '__main__':
    iterations = 2
    print(srinivasa(iterations))