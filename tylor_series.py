# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:33:37 2022

@author: EMRE5
"""
#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt

from sympy import *

# def taylor2(f,n,x0,x_data):
#     if n>0:        
#         return taylor(f,n-1,x0,x_data)+((((x_data-x0)**n)*lambdify(x,f.diff(x,n))(x0))/math.factorial(n))
#     else:
#         return lambdify(x,f)(x0)

def taylor(f,n,x0,x_data):
    return sum([lambdify(x,f.diff(x,i))(x0)*np.power(x_data-x0,i)/math.factorial(i) for i in range(n+1)])

x=Symbol('x')
f=E**x
# f=-.1*x**4 -.15*x**3 -.5*x**2 -.25*x + 1.2

x0=0#¨np.ones(11)*0

x_data=np.linspace(0,1,11)
fig3= plt.figure()
#plt.plot(x_data,math.e**x_data,label="f1")
plt.plot(x_data,lambdify(x,f)(x_data),label="f1")
for n in range(5):   
    plt.plot(x_data,taylor(f,n,x0,x_data), label="n="+str(n))
plt.grid()
plt.legend()
plt.show()