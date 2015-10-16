#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

GMm = 1

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciones de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        r = np.sqrt(x**2+y**2)
        cosp = x/r
        senp = y/r
        fp = 2*self.alpha/r**3 - 1/r**2
        fx = fp*GMm*cosp
        fy = fp*GMm*senp
        return np.array([vx, vy, fx, fy])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        x, y, vx, vy = self.y_actual
        dx, dy, dvx, dvy = self.ecuacion_de_movimiento()
        self.y_actual = np.array([x+dt*dx, y+dt*dy, vx+dt*dvy, vy+dt*dvx])
        self.t_actual += dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        pos = np.array(self.y_actual)
        K1 = self.ecuacion_de_movimiento()
        self.y_actual = pos + dt*K1/2.
        K2 = self.ecuacion_de_movimiento()
        self.y_actual = pos + dt*K2/2.
        K3 = self.ecuacion_de_movimiento()
        self.y_actual = pos + dt*K3
        K4 = self.ecuacion_de_movimiento()
        self.y_actual = pos + (K1+2*K2+2*K3+K4)*dt/6.
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        pass
