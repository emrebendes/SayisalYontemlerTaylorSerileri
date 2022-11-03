# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:51:30 2022

@author: EMRE5
"""
#%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt
from sympy import *



MAX_ITER=150
x=Symbol('x')
# f=x**.5
f=E**x
# x0=4

x0=0

x_data=0.1
anlamlı_basamak = 3
Es= 10**-(anlamlı_basamak+1)
Ea=10
n=0
ty=0

print("    taylor \t\t Ea \t\t\t Es") 
while(Es<Ea and n<MAX_ITER):
    tyn=ty+lambdify(x,f.diff(x,n))(x0)*np.power(x_data-x0,n)/math.factorial(n)
    Ea=abs(tyn-ty)
    ty=tyn
    print("%d - %2.8f \t %2.8f \t %2.8f" % (n,ty,Ea,Es) ) 
    n+=1
    