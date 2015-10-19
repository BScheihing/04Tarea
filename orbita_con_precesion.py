#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

condicion_inicial = [10.0, 0.0, 0.0, 0.3]

Mercury = Planeta(condicion_inicial,10**(-2.350))
x_pos = [Mercury.y_actual[0]]
y_pos = [Mercury.y_actual[1]]
energia = [Mercury.energia_total()]
dt=0.01
Mercury.avanza_rk4(dt)
for i in range(600000):
    x_pos.append(Mercury.y_actual[0])
    y_pos.append(Mercury.y_actual[1])
    energia.append(Mercury.energia_total())
    Mercury.avanza_verlet(dt)

x_pos = np.array(x_pos)
y_pos = np.array(y_pos)
energia = np.array(energia)

#Calculo de momentos en perihelio y frecuencia de precesion
r = np.sqrt(np.power(x_pos,2)+np.power(y_pos,2))
r_maximo = max(r)
esta_en_perihelio = False
tiempos_perihelio = []
angulos_perihelio = []
counter=0

for i in range(len(r)):
    angulo_actual = np.arctan2(y_pos[i],x_pos[i])
    if counter>=1:
        ultimo_perihelio = angulos_perihelio[counter-1]
        out_perihelio = np.mod(ultimo_perihelio + np.pi +
        np.pi/2 ,2*np.pi) - np.pi
    if not esta_en_perihelio:
        if abs(r[i] - r_maximo)<10**(-6):
            esta_en_perihelio = True
            tiempos_perihelio.append(i*dt)
            angulos_perihelio.append(angulo_actual)
            counter+=1
    elif out_perihelio<=angulo_actual:
        if abs(r[i] - r_maximo)>=10**(-6):
            esta_en_perihelio = False

t = np.array(tiempos_perihelio)
angulos = np.array(angulos_perihelio)
vel_angular_prec = (angulos[2:]-angulos[1:-1])/(t[2:]-t[1:-1])

print "Velocidad angular de precesion:", np.mean(vel_angular_prec), "[rad/s]"
print "Desviacion estandar de velocidad angular de precesion", np.std(vel_angular_prec), "[rad/s]"
print "Tiempo entre perihelios:", np.mean(t[2:]-t[1:-1]), "[s]"
print "Angulo precesado por orbita:", np.mean(angulos[2:]-angulos[1:-1]), "[rad]"

plt.figure(1)
plt.plot(x_pos,y_pos)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title(u'Ó''rbita perturbada, ''$\\alpha = 10^{-2.350}$')
plt.show()
plt.figure(2)
plt.plot(np.array(range(600001))*dt,energia)
plt.xlabel('Tiempo [s]')
plt.ylabel('Energ'u'í''a [J]')
plt.ylim([-0.1,0])
plt.title('Evoluci'u'ó''n de la energ'u'í''a total en el tiempo, \
''$\\alpha = 10^{-2.350}$')
plt.show()
