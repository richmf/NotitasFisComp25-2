#!/usr/bin/env python
# coding: utf-8
import math as m
import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
from matplotlib import animation

def caida_libre(t , x_v , g=9.81 , gam = 0):
    # x_v = [x,y,vx,vy]
    dx = x_v[2]
    dy = x_v[3]
    dvx = -gam*x_v[2]
    dvy = -g -gam*x_v[3]
    return np.array([dx,dy,dvx,dvy])

def suelo(t,x_v, g=9.81 , gam = 0):
    return x_v[1]

def caida_con_rebote(ci , t_final , g=9.81 , gam = 0, reb_tot=10):
    x , y , reb = np.array([]) , np.array([]) , 0 
    while reb < reb_tot:
        x_v = sp.solve_ivp(caida_libre,(0,t_final),ci,dense_output=True,events=suelo,args=(g,gam,))
        t_reb = x_v.t_events[0][-1]
        t = np.arange(0,t_reb,0.05)
        x_n , y_n , vx_n , vy_n = x_v.sol(t)
        x , y  = np.concatenate((x,x_n)) , np.concatenate((y,y_n)) 
        n_ci = x_v.sol(t_reb)
        n_ci[3] = -n_ci[3]
        t_final , ci = 2.1*t_reb , n_ci
        reb += 1
    x , y  = np.concatenate((x,np.array([n_ci[0]]))) , np.concatenate((y,np.array([n_ci[1]]))) 
    return x , y

tf = 1
ci = [0.0,0.0,0.2,4.0]
x , y = caida_con_rebote(ci,tf,gam=0.3,reb_tot=20)

figura , ejes = plt.subplots()
ejes.set_xlim([x[0],x[-1]]) , ejes.set_ylim([0,y.max()+0.1])
pelota, = ejes.plot([],[],'o')
linea, = ejes.plot([],[],'--')

def peli(i):
    pelota.set_data(x[i-1:i],y[i-1:i])
    linea.set_data(x[:i],y[:i])
    return (pelota,linea,)

mi_pelicula = animation.FuncAnimation(figura,peli,frames=len(x),interval=40)
plt.show()



