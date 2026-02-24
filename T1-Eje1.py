# Tarea 1. Ejercicio 1

import numpy as np 
import matplotlib.pyplot as plt

x1 = np.linspace(-4*np.pi,4*np.pi,100)
y = 1/np.tan(x1)  

#en clase usabamos diff()<0 ya que la función tan(x) es creciente
#y queríamos quitar las partes crecientes que completaba python
#pero 1/tan(x) es decreciente, por lo que ahora usaré diff()>0
#para quitar las partes crecientes 

y[:-1][np.diff(y)>0]=np.nan
z=np.zeros_like(x1)
plt.plot(x1,z, color='black')
plt.plot(x1,y, color='blue', label=r'$\frac{1}{\tan(x)}$')
plt.ylim(-2, 2)  
plt.grid()
plt.legend()
plt.show()

