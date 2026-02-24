# Tarea 1. Ejercicio 2

import numpy as np 
import matplotlib.pyplot as plt

x1= np.linspace(-5,5,200)      #creación del dominio  

#Lo que hice fue ir modificando el dominio a con if y for hasta obtener los valores que quería que arrojara 
#la función 

x_1= np.floor(x1)          #creación de la función escalón, con floor() se redondea hacia abajo cada valor del dominio  
y0=[]                       #hice este arreglo vacío para ahí meter los valores del x_1 modificados 

for i in x_1:                # El for cada valor de x_1 para volverlo 1 en el caso de que sea par. En cualquier otro 
    if i % 2 == 0:            #caso, dejé el valor de x_1 sin modificar.
        j=1
        y0.append(j+1)        #Éste j+1 es para que el valor se vuelva par y así no choque con el otro for
    else:
        j=i
        y0.append(j)
y0=np.array(y0)

#Hasta aquí tengo los valores de mi dominio moficados en función de si son pares o impares. 
#Ahora, con el siguiente for, lo que hice fue volver 1 los valores impares y dejar los pares sin modificar.
#(para ésto sumé un 1 a los valores anteriores, si lo dejaba con un 1, el siguiente for iba a modificar los 1)

y0=np.array(y0)
y1=[]    #Aquí voy a almacenar los valores de y0 modificados

for i in y0:                  #Con éste for ahora modifico los impares a 1. No los hago 0, porque eso lo haré restando un 1
    if i % 2 != 0:            # a todo el array y1
        j=1
        y1.append(j)
    else:
        j=i
        y1.append(j)
y1=np.array(y1)
y1=y1-1                     #Aquí es donde resto un 1 a todo el array con el objetivo de ahora sí tener ceros y unos

y1[:-1][np.diff(y1)<0]=np.nan
y1[:-1][np.diff(y1)>0]=np.nan        #Con éstas dos lineas, quito los valores extremos, para que no se produzcan 
                                    #lineas verticales en el gráfico 


plt.plot(x1,y1)
plt.grid()
plt.show()
