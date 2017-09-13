#Librerias
import matplotlib.pyplot as plt 
import numpy as np

def f(t):
    return  2015 * np.cos(3*t)
#Definimos el rango de una variables y el intervalo en el que cambian
t1 = np.arange(0.0,15.0,0.004)
#Grafica la variable t contra la funcion f(t) con estrellas
plt.plot(t1, f(t1), 'm*')
#guarda la grafica
plt.savefig('examen.png')
#muestra la grafica
plt.show()

