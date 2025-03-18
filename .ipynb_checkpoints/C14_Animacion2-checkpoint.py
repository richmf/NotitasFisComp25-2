import math as m
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

t = np.linspace(0,4*np.pi,200)
x = np.linspace(0,2*np.pi,100)

figura , ejes = plt.subplots()
ejes.set_xlim([x[0],x[-1]]) , ejes.set_ylim([-1.1,1.1])
linea, = ejes.plot([],[])

def peli(i):
    y = np.sin(x)*np.cos(t[i])
    linea.set_data(x,y)
    return (linea,)

mi_pelicula = animation.FuncAnimation(figura,peli,frames=len(t),interval=16)
#mi_pelicula.save(filename="mi_peli.html",writer="html")
#mi_pelicula.save(filename="mi_peli.gif",writer="pillow")
mi_pelicula.save(filename="mi_peli.mp4",writer="ffmpeg")
#plt.show()