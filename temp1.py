#Librerias
import matplotlib.pyplot as plt 
import numpy as np

#Esta definic'on no tiene las caraccter'isticas indicadas en el enunciado del examen. Una deficni'on m'as apropiada ser'ia : 2*np.cos(2*np.pi*t)+2015
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

