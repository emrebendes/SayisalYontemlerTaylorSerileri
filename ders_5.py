%matplotlib qt
import numpy as np
import math
import matplotlib.pyplot as plt

coef = [-.1, -.15, -.5, -.25, 1.2]
f = np.poly1d(coef)
d = [f.deriv(i) for i in range(len(coef))]
x= np.linspace(0,1,11)
def taylor(n,x,x0):
    return sum([d[i](x0)*np.power(x-x0,i)/math.factorial(i) for i in range(n+1)])

fig1 = plt.figure()
plt.plot(x,f(x),label="f(x)")

for n in range(len(coef)):
    plt.plot(x,taylor(n,x,0),label="n="+str(n))

plt.grid()
plt.legend()
plt.show()