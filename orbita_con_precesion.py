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
dt=0.1
Mercury.avanza_rk4(dt)
for i in range(100000):
    x_pos.append(Mercury.y_actual[0])
    y_pos.append(Mercury.y_actual[1])
    energia.append(Mercury.energia_total())
    Mercury.avanza_verlet(dt)

x_pos = np.array(x_pos)
y_pos = np.array(y_pos)
energia = np.array(energia)

plt.figure(1)
plt.plot(x_pos,y_pos)
plt.show()
plt.figure(2)
plt.plot(range(100001),energia)
plt.show()
