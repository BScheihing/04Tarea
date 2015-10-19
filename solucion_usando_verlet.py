#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
x_pos.append(Mars.y_actual[0])
y_pos.append(Mars.y_actual[1])
energia.append(Mars.energia_total())
Mars.avanza_rk4(dt)
for i in range(10000):
    x_pos.append(Mars.y_actual[0])
    y_pos.append(Mars.y_actual[1])
    energia.append(Mars.energia_total())
    Mars.avanza_verlet(dt)

x_pos = np.array(x_pos)
y_pos = np.array(y_pos)
energia = np.array(energia)

#Resultados
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(x_pos,y_pos)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim([-10,12])
ax.set_ylim([-12,12])
ax.set_aspect('equal')
ax.set_title(u'Ó''rbita descrita por planeta (m'u'é''todo de Verlet)')
plt.savefig('Orb_Verlet.eps')
plt.show()
plt.figure(2)
plt.plot(np.array(range(10001))*dt,energia)
plt.xlabel('Tiempo [s]')
plt.ylabel('Energ'u'í''a [J]')
plt.ylim([-0.1,0])
plt.title('Evoluci'u'ó''n de la energ'u'í''a total en el tiempo')
plt.savefig('Energ_Verlet.eps')
plt.show()
