# Tarea 1. Ejercicio 4

#Para éste ejercicio intenté constuír la función Ai
#no pude, así que usé la que tenía scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import airy

#Ai(x)

x = np.linspace(-20, 10, 200)
y = np.zeros_like(x)
Ai = airy(x)[0]     #Función Ai(x)  
plt.plot(x,y)
plt.plot(x, Ai)
plt.grid()
plt.show()

#Funciones de Bessel de primer especie 

from scipy.special import jv

n = np.array([0,1,2,3])
x = np.linspace(0,20,200)
y = np.zeros_like(x)

for i in n:
    j = jv(i,x)
    plt.plot(x,j,label=r'$n$ = %2.2f' %i)
plt.plot(x,y, color='black')
plt.legend()
plt.grid()
plt.show()

#Funcion de Bessel esferica primera especie

from scipy.special import spherical_jn

n = np.array([0,1,2,3])
x = np.linspace(0,20,200)
y = np.zeros_like(x)

for i in n:
    j = spherical_jn(i,x)
    plt.plot(x,j,label=r'$n$ = %2.2f' %i)
plt.plot(x,y, color='black')
plt.legend()
plt.grid()
plt.show()
