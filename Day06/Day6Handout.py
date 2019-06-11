# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:47:22 2019

@author: kmh02
"""
"""
1) Implement a function integrator using trapezoid rule 
"""
import numpy as np
import math 

def f(x,a=1): 
    return a*x**2
xs=np.arange(10)
ys=f(xs)

dx=1
trap=dx*(f(xs+dx) +f(xs)) / 2

print (trap)

"""
2) Implement a function integrator using Simpson's rule. 
"""
a= xs[0]
b=xs[-1]
h = (b-a)/3
factor = (f(a) + 3*f((2*a + b) / 3) + 3*f((a + 2*b) / 3) + f(b))
integral = (3 * h / 8) * factor

print (integral)


"""
3) Implement a root finder using Newton's method
"""
def f_derivative (x,a=1):
    return 2*a*x

guess1 = 1    
tolerance= 0.001
guess2 = guess1-f(guess1)/f_derivative(guess1)
difference = guess1-guess2
print (difference)


while (difference > tolerance):
   guess2 = guess1-f(guess1)/f_derivative(guess1)
   difference=guess1-guess2
   print(difference)
   guess1=guess2
   print(guess2)
   
"""
4) Implement a root finder using the secant method
"""
x0=1
x1=2
x2 = x1 - f(x1) * (x1 - x0)/( f(x1) - f(x0) )
difference = x2-x1
print (difference)

while (difference > tolerance):
   x_new = [] 
   x2 = x1 - f(x1) * (x1 - x0)/( f(x1) - f(x0) ) 
   difference = x2-x1
   print (difference)
   x1=x2
   x0=x1
   print (x2)

#this isn't finished
   


