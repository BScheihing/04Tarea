#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

condicion_inicial = [10.0, 0.0, 0.0, 0.3]

Mars = Planeta(condicion_inicial)
x_pos = []
y_pos = []
energia = []
dt=0.1
Mars.avanza_rk4(dt)
for i in range(10000):
    x_pos.append(Mars.y_actual[0])
    y_pos.append(Mars.y_actual[1])
    energia.append(Mars.energia_total())
    Mars.avanza_verlet(dt)

x_pos = np.array(x_pos)
y_pos = np.array(y_pos)
energia = np.array(energia)

plt.figure(1)
plt.plot(x_pos,y_pos)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title(u'Ó''rbita descrita por planeta (m'u'é''todo de Verlet)')
plt.show()
plt.figure(2)
plt.plot(np.array(range(10000))*0.1,energia)
plt.xlabel('Tiempo [s]')
plt.ylabel('Energ'u'í''a [J]')
plt.title('Evoluci'u'ó''n de la energ'u'í''a total en el tiempo')
plt.show()
