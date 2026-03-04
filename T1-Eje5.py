# Tarea 1. Ejercicio 5. 
# utilizando los coeficientes de https://en.wikipedia.org/wiki/Finite_difference_coefficient 
# para h4

import numpy as np 
import matplotlib.pyplot as plt

#Lo único que cambia de mi derivada y la que se vió en clase h4, son
#los coeficientes

def deriv_h4(f,x):
    df = np.zeros_like(f)
    h = x[1]-x[0]
    for i in range (2, len(f)-2):
        df[i] = (1/12)*f[i-2] - (2/3)*f[i-1] + (2/3)*f[i+1] - (1/12)*f[i+2]
    df[0] = -(25/12)*f[0] + 4*f[1] - 3*f[2] + (4/3)*f[3] - 0.25*f[4]
    df[1] = -(25/12)*f[1] + 4*f[2] - 3*f[3] + (4/3)*f[4] - 0.25*f[5]
    df[-1] = (25/12)*f[-1] - 4*f[-2] + 3*f[-3] - (4/3)*f[-4] + 0.25*f[-5]
    df[-2] = (25/12)*f[-2] - 4*f[-3] + 3*f[-4] - (4/3)*f[-5] + 0.25*f[-6]
    return df/h

#Aquí pruebo la derivada

x = np.linspace(0,10,200)
y = np.sin(x)
y1 = deriv_h4(y,x)
y2 = np.cos(x)
plt.plot(x,y, label = "cos")
plt.plot(x,y1, label = "derivada" )
plt.plot(x,y2, '.',label = "sen")
plt.legend()
plt.show()

# comparación entre algoritmo de clase y hecho aquí en mi tarea 
# ésto lo hago para sacarme de la duda de si son las mismas jaja 

def deriv_h4_clase(f,x):
    df = np.zeros_like(f)
    h = x[1]-x[0]
    for i in range(2,len(f)-2):
        df[i] = f[i-2] - 8*f[i-1] + 8*f[i+1] - f[i+2]
    df = df/12
    df[0] = -(25/12)*f[0] + 4*f[1] - 3*f[2] + (4/3)*f[3] - 0.25*f[4]
    df[1] = -(25/12)*f[1] + 4*f[2] - 3*f[3] + (4/3)*f[4] - 0.25*f[5]
    df[-1] = (25/12)*f[-1] - 4*f[-2] + 3*f[-3] - (4/3)*f[-4] + 0.25*f[-5]
    df[-2] = (25/12)*f[-2] - 4*f[-3] + 3*f[-4] - (4/3)*f[-5] + 0.25*f[-6]
    return df/h

x = np.linspace(0,10,200)
y_tarea = deriv_h4(y,x)
y_clase = deriv_h4_clase(y,x)
plt.plot(x,abs(y_clase-y2), label = "clase")
plt.plot(x,abs(y_tarea-y2), label = "clase")   
plt.legend()
plt.show()