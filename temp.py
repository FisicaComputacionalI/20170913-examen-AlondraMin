#Librerias
import numpy as np
import pylab as pl
#Valores del eje X en este caso la edad
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Valores en el eje Y para cada valor en el eje X en este caso los anioss
y=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
#Grafica del vector x contra el vector y establecer un color en cada punto
pl.plot(x,y, 'bD')
#Grafica del vector x contra el vector y
pl.plot(x,y)
pl.ylabel('Anios')
pl.xlabel('Edad')
pl.title('Alondra Dominguez Gonzalez')
#Guarda la grafica
pl.savefig('temp1.png')
