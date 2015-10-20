#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este script utiliza la clase Planeta para resolver la órbita de un planeta de
masa 1 kg, orbitando un cuerpo central de masa M = 1.498 x 10^10 kg. El
movimiento es determinado usando un método Runge-Kutta orden 4. Al final se
presentan los resultados en forma de gráficos de la órbita y de la energía en
el tiempo.
'''

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

#Solucion a trayectoria
condicion_inicial = [10.0, 0.0, 0.0, 0.3]

Mars = Planeta(condicion_inicial)
x_pos = []
y_pos = []
energia = []
dt=0.1
for i in range(10000):
    x_pos.append(Mars.y_actual[0])
    y_pos.append(Mars.y_actual[1])
    energia.append(Mars.energia_total())
    Mars.avanza_rk4(dt)

x_pos = np.array(x_pos)
y_pos = np.array(y_pos)
energia = np.array(energia)

#Resultados
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(x_pos,y_pos)
ax.plot(0,0,'o',color='r',linewidth=2.0)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim([-10,12])
ax.set_ylim([-12,12])
ax.set_aspect('equal')
ax.set_title(u'Ó''rbita descrita por planeta (m'u'é''todo RK4)')
plt.savefig('Orb_RK4.eps')
plt.show()
plt.figure(2)
plt.plot(np.array(range(10000))*dt,energia)
plt.xlabel('Tiempo [s]')
plt.ylabel('Energ'u'í''a [J]')
plt.ylim([-0.1,0])
plt.title('Evoluci'u'ó''n de la energ'u'í''a total en el tiempo')
plt.savefig('Energ_RK4.eps')
plt.show()
