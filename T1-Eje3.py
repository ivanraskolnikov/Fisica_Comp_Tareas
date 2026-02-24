# Tarea 1. Ejercicio 3

import numpy as np 
import matplotlib.pyplot as plt
n = np.array([3,5,10,20,30])       #Para poder graficar con un for 
x = np.linspace(-np.pi,np.pi,200)

def S_n (x,n):      #Definición de la suma
    S=0
    for i in range(0,n+1):
        S += (((-1)**i)/((2*i+1)**2))*np.sin((2*i+1)*x)
    return(S)
 
for i in n:               #Usé parte del código para hacer varias gráficas en un plot
    y = S_n(x,i)          #solo que lo grafiqué todo dentro del for, porque al poner todas
    plt.plot(x,y,label=r'$n$ = %2.1f' %i)     #en un solo gráfico, no se ve bien 
    plt.legend()
    plt.grid()
    plt.show()