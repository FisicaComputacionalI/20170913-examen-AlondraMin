#Librerias
import matplotlib.pyplot as plt 
import numpy as np

def f(t):
    return  2015 * np.cos(3*t)
#Definimos el rango de una variables y el intervalo en el que cambian
t1 = np.arange(0.0,15.0,0.004)
t2 = np.arange(0.0,15.0,0.002)

#Crean el grupo de graficas
plt.figure(1)
#Crea el lienzo con dos renglones, una columna y entra a la primera seccion de esta division
plt.subplot(211)
#Grafica la variable t1 contra la funcion f(t1) con circulos azules y grafica la variable t2 contra la funcion f(t2) con una linea negra
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

#Entra a la segunda seccion del lienzo dividido
plt.subplot(212)
#grafica la variable t2 contra la funcion cos(2pi*x) con una linea punteada roja
plt.plot(t2, np.cos(2*t2), 'r--')

#guarda la grafica
plt.savefig('examen.png')
#muestra la grafica
plt.show()

