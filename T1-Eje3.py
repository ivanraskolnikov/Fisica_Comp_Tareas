# Tarea 1. Ejercicio 3

import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,200)

def S_n (x,n):
    S=0
    for i in range(0,n+1):
        S += (((-1)**i)/((2*i+1)**2))*np.sin((2*i+1)*x)
    return(S)

y = S_n(x,3) 

plt.plot(x,y)
plt.grid()
plt.show()